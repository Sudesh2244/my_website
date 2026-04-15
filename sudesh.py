import streamlit as st
from huggingface_hub import InferenceClient

st.title("Hugging Face Inference API Demo")
st.write("This app demonstrates how to use the Hugging Face Inference API to generate images from text prompts.")

# Input field for Hugging Face API key
hf_api_key = st.text_input("Enter your Hugging Face API key:", type="password")

# Input field for text prompt
prompt = st.text_input("Enter your text prompt:", "Astronaut riding a horse")

if st.button("Generate Image"):
    if not hf_api_key:
        st.error("Please enter your valid Hugging Face API key.")
    else:
        client = InferenceClient(token=hf_api_key)
        try:
            st.write(f"Generating image for: '{prompt}'")
            image = client.text_to_image(
                prompt=prompt,
                model="black-forest-labs/FLUX.1-schnell"
            )
            st.image(image, caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error generating image: {str(e)}")

import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🎨 AI Image Generator")
st.write("Generate images using Hugging Face API")

hf_api_key = st.text_input("Enter your Hugging Face API key:", type="password")
prompt = st.text_input("Enter your prompt:", "Astronaut riding a horse")

if st.button("Generate Image"):
    if not hf_api_key:
        st.error("❌ Please enter your API key")
    elif not prompt:
        st.error("❌ Please enter a prompt")
    else:
        try:
            with st.spinner("⏳ Generating image..."):
                client = InferenceClient(token=hf_api_key)

                image = client.text_to_image(
                    prompt=prompt,
                    model="stabilityai/stable-diffusion-2"
                )

                st.success("✅ Image generated!")
                st.image(image, caption=prompt, use_column_width=True)

        except Exception as e:
            st.error("❌ Failed to generate image")
            st.exception(e)  # shows real error

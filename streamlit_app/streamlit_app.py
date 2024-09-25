import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

st.title("Article Image and Caption Generator")

# Inputs
url = st.text_input("Enter the article URL")
num_sentences = st.number_input("Number of sentences to summarize to", min_value=1, value=3)
steps = st.number_input("Steps for image generation", min_value=1, value=50)
seed = st.number_input("Random seed for generation", min_value=0, value=42)
aspect_ratio = st.selectbox("Select Aspect Ratio", ["16:9", "4:3", "1:1"])

if st.button("Generate Image and Caption"):
    with st.spinner("Generating..."):
        # API request
        response = requests.post(
            "http://fastapi:8000/generate_image_caption",  # Use service name defined in docker-compose
            json={
                "url": url,
                "num_sentences": num_sentences,
                "steps": steps,
                "seed": seed,
                "aspect_ratio": aspect_ratio
            }
        )

        if response.status_code == 200:
            data = response.json()
            caption = data["caption"]
            image_data = base64.b64decode(data["image"])
            image = Image.open(BytesIO(image_data))

            st.image(image, caption=caption, use_column_width=True)
        else:
            st.error(f"Error: {response.json()['detail']}")
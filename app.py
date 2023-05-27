import streamlit as st

from PIL import Image

import requests

from io import BytesIO

# Define the GitHub repository URL

github_url = "https://raw.githubusercontent.com/your_username/your_repository/master/"

# Define the list of available images

images = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Function to download the image from GitHub

def download_image(url):

    response = requests.get(url)

    img = Image.open(BytesIO(response.content))

    return img

# Streamlit app

def main():

    st.title("Image Compressor")

    # Select image from dropdown

    selected_image = st.selectbox("Select an image:", images)

    # Build the GitHub image URL

    image_url = github_url + selected_image

    # Download and display the selected image

    image = download_image(image_url)

    st.image(image, caption=selected_image, use_column_width=True)

    # Image compression options

    quality = st.slider("Select the image quality (0-100):", 0, 100, 80)

    # Compress the image

    compressed_image = image.copy()

    compressed_image.save("compressed_image.jpg", optimize=True, quality=quality)

    # Display the compressed image

    st.image(compressed_image, caption="Compressed Image", use_column_width=True)

if __name__ == "__main__":

    main()


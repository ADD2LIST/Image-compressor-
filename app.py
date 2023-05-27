import streamlit as st

from PIL import Image

import io

# Streamlit app

def main():

    st.title("Image Compressor")

    # File uploader for image selection

    uploaded_file = st.file_uploader("Select an image:", type=["jpg", "jpeg", "png"])

    # Process the uploaded image

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(image, caption="Original Image", use_column_width=True)

        # Image compression options

        quality = st.slider("Select the image quality (0-100):", 0, 100, 80)

        # Compress the image

        compressed_image = compress_image(image, quality)

        # Display the compressed image

        st.image(compressed_image, caption="Compressed Image", use_column_width=True)

        # Button to save the compressed image

        if st.button("Save Compressed Image"):

            save_image(compressed_image)

# Function to compress the image

def compress_image(image, quality):

    # Create a BytesIO object to store the compressed image data

    compressed_image_stream = io.BytesIO()

    # Save the compressed image to the BytesIO stream

    image.save(compressed_image_stream, format="JPEG", optimize=True, quality=quality)

    # Rewind the stream to the beginning

    compressed_image_stream.seek(0)

    # Open the compressed image from the stream

    compressed_image = Image.open(compressed_image_stream)

    return compressed_image

# Function to save the image

def save_image(image):

    image.save("compressed_image.jpg")

    st.success("Image saved successfully!")

if __name__ == "__main__":

    main()



 

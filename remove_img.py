import streamlit as st
from PIL import Image
from rembg import remove
from io import BytesIO
import base64


def download_image(image):
	buffer = BytesIO()
	image.save(buffer,format ="PNG")
	img_byte = buffer.getvalue()
	return img_byte


def display_image(image,left,right):

	img = Image.open(image)
	left.write("Uploaded Image :fire: ")
	left.image(img)

	rembg_img = remove(img)
	right.write("Resulted Image :fire: ")
	right.image(rembg_img)
	return rembg_img


if __name__ == "__main__":

	st.set_page_config(page_title="Remove Background from Image")

	st.write("## Remove Background from Image")

	left,right = st.columns(2)
	image = st.file_uploader("Upload image" , type=["jpg","jpeg","png"])

	if image is not None:
		img = display_image(image=image,left=left,right=right)
		st.download_button("Download Image", download_image(img), "a.png", "image/png")
	else:
		display_image(image="./cat.jpg",left=left,right=right)



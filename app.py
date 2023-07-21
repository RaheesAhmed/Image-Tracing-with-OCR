import streamlit as st
from PIL import Image
import pytesseract
import easyocr
import cv2
import numpy as np


def extract_text_with_pytesseract(image):
    text = pytesseract.image_to_string(image)
    return text


def extract_text_with_easyocr(image):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image)
    text = " ".join([res[1] for res in result])
    return text


def image_to_text(image, ocr_technique):
    if ocr_technique == "PyTesseract":
        return extract_text_with_pytesseract(image)
    elif ocr_technique == "EasyOCR":
        return extract_text_with_easyocr(image)

    else:
        return "Invalid OCR technique selected."


def main():
    st.title("Image to Text Converter")
    st.write("Upload an image and select an OCR technique to extract text.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            image_array = np.array(image)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            ocr_technique = st.selectbox(
                "Select OCR Technique:",
                [
                    "PyTesseract",
                    "EasyOCR",
                ],
            )
            if st.button("Extract Text"):
                text = image_to_text(image_array, ocr_technique)
                st.subheader("Extracted Text:")
                st.text(text)
        except Exception as e:
            st.error(f"Error: {e}")
            st.write("Please upload a valid image file.")


if __name__ == "__main__":
    main()

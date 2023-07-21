# OCR Web App using Streamlit

This is a simple web application built with Streamlit that allows users to upload images and extract text from them using different OCR techniques such as PyTesseract, EasyOCR, and PaddleOCR.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RaheesAhmed/Image-Tracing-with-OCR
   cd Image-Tracing-with-OCR
   ```
2. Install the required libraries:

   ```bash
   pip install streamlit pytesseract easyocr paddleocr awscli google-cloud-vision

   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. After running the app, it will open in your default web browser.

2. Upload an image by clicking the "Choose an image..." button.

3. Select an OCR technique from the drop-down menu (PyTesseract, EasyOCR, or PaddleOCR).

4. Click the "Extract Text" button to see the extracted text below the uploaded image.

5. The app will display the extracted text using the chosen OCR technique.

## Additional Notes

The OCR accuracy may vary depending on the image quality and complexity. For the best results, use images with clear, well-defined text.

For AWS Textract and Google Cloud Vision API, you need to set up credentials and obtain the API key, respectively.

The PaddleOCR technique may require additional libraries based on your system configuration. Follow the official PaddleOCR installation guide for more details.

Feel free to customize and extend the app to suit your specific requirements.

## License

This project is licensed under the MIT License.

Feel free to add more sections or details to the README.md file as needed. The provided template covers the basic information about the OCR web app, installation steps, usage instructions, and additional notes. Adjust the details according to your specific project and any additional features you might add.

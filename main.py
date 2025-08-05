import streamlit as st
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(file_obj):

    reader = PyPDF2.PdfReader(file_obj)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

st.title("PDF Text Extractor")
st.write("Upload a PDF file to extract and display its text.")


uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    
    file_bytes = BytesIO(uploaded_file.getvalue())

    extracted_text = extract_text_from_pdf(file_bytes)

    if extracted_text:
        st.subheader("Extracted Text")
        st.text_area("PDF Content", extracted_text, height=600)
    else:
        st.warning("Could not extract text from the PDF. The file might be an image-based PDF.")

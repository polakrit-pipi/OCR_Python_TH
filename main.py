import streamlit as st
from PIL import Image
import pytesseract


class OCR:

    def __init__(self):
        st.set_page_config(page_title="Python OCR")
        self.textto = ""

    def inicial(self):
        st.title("OCR Program")
        st.write("Optical Character Recognition (OCR) Python")
        imageme = st.file_uploader("Select file type", type=["png","jpg"])
        if imageme:
            img = Image.open(imageme)
            st.image(img, width=350)
            st.info("Text transform")
            self.textto = self.extract_img(img)
            st.write("{}".format(self.textto))
            
      
    
    def extract_img(self, img):
        textto = pytesseract.image_to_string(img, lang="tha+eng")
        return textto
    
   
ocr = OCR()
ocr.inicial()

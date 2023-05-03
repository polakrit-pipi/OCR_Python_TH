import streamlit as st
from PIL import Image
import pytesseract


class OCR:

    def __init__(self):
        st.set_page_config(page_title="Python OCR")
        self.texto = ""

    def inicial(self):
        st.title("OCR Programa")
        st.write("Optical Character Recognition (OCR) Python")
        imagem = st.file_uploader("Select file type", type=["png","jpg"])
        if imagem:
            img = Image.open(imagem)
            st.image(img, width=350)
            st.info("Text transform")
            self.texto = self.extract_img(img)
            st.write("{}".format(self.texto))
            
      
    
    def extract_img(self, img):
        texto = pytesseract.image_to_string(img, lang="tha+eng")
        return texto
    
   
ocr = OCR()
ocr.inicial()

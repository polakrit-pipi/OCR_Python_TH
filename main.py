#import principal
import streamlit as st
#imports relacionados
from PIL import Image
import pytesseract
#metodos internos


class OCR:

    def __init__(self):
        #altera titulo da pagina
        st.set_page_config(page_title="Python OCR")
        #inicializa variveis
        self.texto = ""
        self.analisar_texto = False

    def inicial(self):
        #conteudo inicial da pagina
        st.title("OCR Programa")
        st.write("Optical Character Recognition (OCR) implementado com Python")
        imagem = st.file_uploader("Selecione alguma imagem", type=["png","jpg"])
        #se selecionar alguma imagem...
        if imagem:
            img = Image.open(imagem)
            st.image(img, width=350)
            st.info("Texto extraído")
            self.texto = self.extrair_texto(img)
            st.write("{}".format(self.texto))
            
            #Opcao de analisar texto
            self.analisar_texto = st.sidebar.checkbox("Analisar texto")
            if self.analisar_texto==True:
                self.mostrar_analise()
    
    def extrair_texto(self, img):
        #O comando que extrai o texto da imagem
        texto = pytesseract.image_to_string(img, lang="tha")
        return texto
    
   
ocr = OCR()
ocr.inicial()

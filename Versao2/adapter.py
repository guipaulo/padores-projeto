#!/usr/bin/python
# -- coding: latin-1 --
import os, sys
import PyPDF2
'''Converter pdf para txt
'''
"""
    Define o tipo de documento usado e receber o mesmo.
    """
class Pdf:
    def _init_(self, tipo):
        self.tipo = tipo
    '''
    Receber de salva documento'''
    def ler_documento(self,documentoleitura):
        with open(documentoleitura, "rb") as pdf_file:
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            number_of_pages = read_pdf.getNumPages()
            page = read_pdf.pages[0]
            self.page_content = page.extractText()
    """
    Converter o documento de pdf para txt e gravar o mesmo.
    """
class Adapter(Pdf):
    def _init_(self,name):
        self.name = name

    def gravar_documento(self,documentosaida):
        self.documentosaida = documentosaida
        user = os.getlogin()
        dir = f"C:\\Users\\{user}\\Documents"
        arq_path = os.path.join(dir, documentosaida)
        with open(arq_path, 'w')  as self.documento:
            self.documento.write(self.page_content)
            return self.page_content
'''
Criar a lista de titulos ou diretorios dos documentos'''
class Listadocumentos(Adapter):
    def _init_(self,documento):
        self.documento = documento

    def gravar_documento_lista(self):
        lista_documentos = []
        lista_documentos.append(self.documento)
        print(lista_documentos)

d1 = Pdf('pdf')
documentopdf = input("digite o nome do documento que deseja converter em formato pdf")
d1.ler_documento(documentopdf)
a1 = Adapter('documento')
a1.ler_documento(documentopdf)
documentotxt = input("digite o nome do documento que deseja salvar em formato txt")
a1.gravar_documento(documentotxt)
l1 = Listadocumentos(a1.gravar_documento)
l1.gravar_documento_lista()
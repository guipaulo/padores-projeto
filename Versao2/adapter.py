#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import PyPDF2
'''Converter pdf para txt
'''
class adapter:
    def __init__(self,name):
        self.name = name
    def ler_arquivo(self,arquivoleitura):
        with open(arquivoleitura, "rb") as pdf_file:
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            number_of_pages = read_pdf.getNumPages()
            page = read_pdf.pages[0]
            self.page_content = page.extractText()
            print(self.page_content)
    def gravar_arquivo(self,arquivosaida):
        with open(arquivosaida, 'w')  as arquivo:
            arquivo.write(self.page_content)

a1 = adapter('pdf')
a1.ler_arquivo("arquivo01.pdf")
a1.gravar_arquivo("ARQUIVO01.txt")

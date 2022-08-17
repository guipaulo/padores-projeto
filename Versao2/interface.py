#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import tkinter
from tkinter import *
from abc import ABC, abstractmethod


class SubscriberJanela1:
    def __init__(self, toplevel):
        self.frame = Frame(toplevel)
        self.frame.pack()
        self.texto = Label(self.frame, text='Bem vindo ao organizador de arquivos!')
        self.texto['width'] = 50
        self.texto['height'] = 5
        self.texto.pack()
        self.botaosalvar= Button(self.frame, text='Salvar arquivo')
        self.botaosalvar['background'] = 'blue'
        self.botaosalvar.pack()
        self.botaobuscar = Button(self.frame, text='Buscar arquivo')
        self.botaobuscar['background'] = 'blue'
        self.botaobuscar.pack()
        self.botaoremover = Button(self.frame, text='Remover arquivo')
        self.botaoremover['background'] = 'blue'
        self.botaoremover.pack()
        #self.botaoazul.bind("<Button-1>", self.update)

    '''
    def update(self, message):
        self.message = message
        self.message = input('digite um texto para copiar na janela 2\n')
        raiz2 = Tk()
        SubscriberJanela2(raiz2, self.message)
        raiz2.mainloop()
'''
'''
class SubscriberJanela2:
    def __init__(self, toplevel, message):
        self.frame = Frame(toplevel)
        self.frame.pack()
        self.texto = Label(self.frame, text='Você está na janela 2')
        self.texto['width'] = 26
        self.texto['height'] = 3
        self.texto.pack()
        self.texto = Label(self.frame, text='O texto abaixo foi copiado da janela 1:')
        self.texto['width'] = 26
        self.texto['height'] = 3
        self.texto.pack()
        self.texto = Label(self.frame, text=message)
        self.texto['width'] = 26
        self.texto['height'] = 3
        self.texto.pack()
        self.botaoazul = Button(self.frame, text='Clique aqui para copiar o texto para a janela 1')
        self.botaoazul['background'] = 'blue'
        self.botaoazul.pack()
        self.frame = Frame(toplevel)
        self.frame.pack()
        self.botaoazul.bind("<Button-1>", self.update)

    def update(self, message):
        self.message = message
        self.message = input('digite um texto para copiar na janela 1\n')
'''



raiz = Tk()
SubscriberJanela1(raiz)
raiz.geometry("500x250+200+200")
raiz.resizable(True,True)

raiz.mainloop()
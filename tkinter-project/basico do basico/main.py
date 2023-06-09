import customtkinter as ctk
from tkinter import *
from tkinter import ttk

#criando uma janela basica
janela = Tk()
janela.title("Minha pagina")
janela.geometry("600x600")


p = ttk.Label(text="Ola,Mundo").place(x=250, y=250)
#posso tambem substituir o (.place(x=250, y=250)) por .grid(row='', column='')

janela.mainloop()

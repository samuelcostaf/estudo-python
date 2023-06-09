import customtkinter as ctk
from tkinter import*
from tkinter import ttk

#criando uma janela basica
janela = Tk()
janela.title("Pagina teste com o tkinter")
janela.geometry("400x400")
janela.resizable(width=False, height=False) #Fixar o tamanho da janela| por consequencia não poderemos maximizar
janela.configure(background="orange",border=0)
#janela.iconbitmap("favicon.ico") --> esta dando bugs

label = ttk.Label(janela, text="Ola, Mundo").place(x=120,y=150)

p = ttk.Label(text="Ola,Mundo").place(x=200, y=150)
#posso tambem substituir o (.place(x=150, y=150)) por .grid(row='', column='')

janela.mainloop()

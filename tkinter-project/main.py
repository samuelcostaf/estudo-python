from tkinter import*
import customtkinter

def clique: 
print("Fazer Login")

janela = customtkinter.Ctk()
janela.geometry("500x500")

texto = customtkinter.CtkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)

botao = customtkinter.CtkButton(janela, text="Login", command="clique")
botao.pack(padx=10 , pady=10)


janela.mainloop()



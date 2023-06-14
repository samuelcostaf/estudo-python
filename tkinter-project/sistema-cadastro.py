import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
import openpyxl, xlrd
import pathlib
from openpyxl import Workbook

#aparencia padrao do sistema
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.aparencia()
        self.sistema_inteiro()

    def layout_config(self):
        self.title('sistema de gestao de cadastro')
        self.geometry("700x500")


    def aparencia(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema:", bg_color="transparent", text_color=['#000', '#fff']).place(x=50, y=430)
        self.opt_apm = ctk.CTkOptionMenu(self, values=['Light', 'Dark', 'System'], command=self.change_apm).place(x=50, y=460)

    def sistema_inteiro(self):
        frame = ctk.CTkFrame(self, width=700, height=50, corner_radius=0, bg_color='orange', fg_color='orange').place(x=0, y=0)
        title = ctk.CTkLabel(frame, text="Cadastro de Clientes", font=("Century Gothic bold", 24), text_color='#fff')

        span = ctk.CTkLabel(self, text="Por favor! Preencha todos os campos do formulario", font=("Century Gothic bold", 24), text_color=['#000', '#fff']).place(x=50, y=70)


    def change_apm(self, new_apm):
        ctk.set_appearance_mode(new_apm)





if __name__=="__main__":
    app = App()
    app.mainloop()
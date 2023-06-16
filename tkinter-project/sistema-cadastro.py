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
        title = ctk.CTkLabel(frame, text="Cadastro de Clientes", font=("Century Gothic bold", 24), text_color='#fff').place(x=190, y=25)

        span = ctk.CTkLabel(self, text="Por favor! Preencha todos os campos do formulario", font=("Century Gothic bold", 24), text_color=['#000', '#fff']).place(x=50, y=70)

        def submit():
            #dados dos entrys
            name = name_entry.get()
            contact = contact_value.get()
            age = idade_value.get()
            endereço = endereço_value.get()
            genero = genero_combobox.get()
            obs = obs_entry.get(0.0, END)


            pass

        def clear():
            pass
            name_entry.set("")
            contact_value.set("")
            idade_value.set("")
            endereço_value.set("")
            obs_entry.get(0.0, END)

        name_value = StringVar
        contact_value = StringVar
        endereço_value = StringVar
        idade_value = StringVar
    #entrys 

        name_entry = ctk.CTkEntry(self, width=350,textvariable=name_value,font=("Century Gohtic", 16), fg_color="transparent")
        contato_entry = ctk.CTkEntry(self, width=200, textvariable=contact_value, font=("Century Gohtic", 16), fg_color="transparent")
        endereço_entry = ctk.CTkEntry(self, width=200, textvariable=endereço_value, font=("Century Gohtic", 16), fg_color="transparent")
        idade_entry = ctk.CTkEntry(self, width=150, textvariable=idade_value, font=("Century Gohtic", 16), fg_color="transparent")

    #Combobox
        genero_combobox = ctk.CTkComboBox(self, values=["Masculino", "Feminino"], font=("arial", 14))
        genero_combobox.set("Masculino")

    #entrada de observações
        obs_entry = ctk.CTkTextbox(self, width=500, height=150, font=("arial", 18), border_color="#aaa", border_width=2, fg_color="transparent")

    #criando as labels
        lb_nome = ctk.CTkLabel(self, text="Nome Completo",  font=("Century Gothic bold", 24), text_color=['#000', '#fff'])

        lb_contato = ctk.CTkLabel(self, text="Contato", font=("Century Gothic bold", 24), text_color=['#000', '#fff'])

        lb_idade = ctk.CTkLabel(self, text="insira sua idade: ", font=("Century Gothic bold", 24), text_color=['#000', '#fff'])

        lb_genero = ctk.CTkLabel(self, text="Gênero", font=("Century Gothic bold"), text_color=['#000', '#fff'])

        lb_endereço = ctk.CTkLabel(self, text="Endereço", font=("Century Gothic bold"), text_color=['#000', '#fff'])

        lb_obs = ctk.CTkLabel(self, text="Observações", font=("Century Gothic bold", 16), text_color=['#000', '#fff'])

        btn_submit = ctk.CTkButton(self, text="Salvar Dados".upper(), command=submit, fg_color="#151", hover_color="#131").place(x=300,y=420) 
        btn_submit = ctk.CTkButton(self, text="Limpar Dados".upper(), command=clear, fg_color="#555", hover_color="#333").place(x=500,y=420)

    #posicionando os elementos na janela
        lb_nome.place(x=50, y=120)
        name_entry.place(x=50, y=150)

        lb_contato.place(x=450, y=120)
        contato_entry.place(x=450, y=150)

        lb_idade.place(x=300,y=190)
        idade_entry.place(x=300,y=220)

        lb_genero.place(x=500,y=190)
        genero_combobox.place(x=500,y=220)

        lb_endereço.place(x=50,y=190)
        endereço_entry.place(x=50,y=220)

        lb_obs.place(x=50, y=260)
        obs_entry.place(x=150,y=260)

    def change_apm(self, new_apm):
        ctk.set_appearance_mode(new_apm)





if __name__=="__main__":
    app = App()
    app.mainloop()
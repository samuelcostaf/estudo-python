import customtkinter as win

jan = win.CTk()

#configurando a janela principal
jan.title(" Projeto Custom-Tkinter")
jan.geometry("700x400")
jan.resizable(width=False, height=False)

jan._set_appearance_mode("dark")

def nova_tela():
    nova_jan = win.CTkToplevel(jan)
    nova_jan.geometry("200x200")

botao_novatela = win.CTkButton(master=jan, text="Abrir nova janela", command=nova_tela).place(x=300,y=100)

jan.mainloop()
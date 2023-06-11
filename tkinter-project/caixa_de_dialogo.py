import customtkinter as win

jan = win.CTk()

jan.title("Interface teste")
jan.geometry("700x400")
jan.resizable(width=False, height=False)

def abrir_caixa():
    dialog = win.CTkInputDialog(title="Caixa de dialogo", text='Insira seu nome completo')
    print("Nome do usuàrio: ", dialog.get_input())

botao = win.CTkButton(jan, text="Cadastro", command=abrir_caixa)
botao.pack(pady=150)




jan.mainloop()
import customtkinter as win

jan = win.CTk()

jan.title("Interface teste")
jan.geometry("700x400")
jan.resizable(width=False, height=False)

win.CTkLabel(jan, text="Data de nascimento: ", font=("sans-serif", 14)).pack(pady=50)


def mes_nasc(escolha):
    print(f"O seu mes de nascimento é: {escolha}")

mes = win.CTkOptionMenu(jan,
                        values= ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'], command=mes_nasc)
mes.pack(pady=5)
mes.set("Mes de nascimento")

jan.mainloop()
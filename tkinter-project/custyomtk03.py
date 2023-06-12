import customtkinter as win

jan = win.CTk()
jan.geometry("500x150")
jan.title("Minha Janela de teste")
jan.resizable(width=False, height=False)

label = win.CTkLabel(jan, text="Prazer em te conhecer: ")
label.pack()

#but = win.CTkButton(jan, text="Clique aqui")
#but.pack(pady=20)

#introduzindo um texto através de um input
#depois, colocando tudo na parte grafica
#text_var = win.StringVar(value=input("Insira seu nome completo: "))

def enviar():
    t = entry.get()
    lab.configure(text=str(t))
    pass

lab = win.CTkLabel(jan,
                    text="",
                    width=200,
                    height=25,
                    text_color="orange")
lab.pack(pady=10)

entry = win.CTkEntry(jan, width=200)
entry.pack()


win.CTkButton(jan,text="Enviar", command=enviar).pack(pady=10)

jan.mainloop()
import customtkinter as win

jan = win.CTk()

jan.title("Caixa de texto")
jan.geometry("700x400")
jan.resizable(width=False, height=False)

caixa_de_texto = win.CTkTextbox(jan, width=300, height=1000, scrollbar_button_color="black", scrollbar_button_hover_color="gray",border_color="black", border_width=1.2, corner_radius=12, fg_color="#FFECD4", text_color="black")
caixa_de_texto.pack()


caixa_de_texto.insert("0.0", "Titulo\n\n" + "Ola, estou neste programa inserindo textos nessa caixa com a ajuda do tkinter.\n\n"*30)


jan.mainloop()
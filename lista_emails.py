import customtkinter



def criar_janela_emails_lista(root_login):
    root_lista = customtkinter.CTkToplevel()
    root_lista.title("LISTA DE EMAILS")
    root_lista.configure(fg_color='#161b33')

    def voltar():
        root_lista.destroy()  # Fechar a janela de lista de e-mails
        root_login.deiconify()

    screen_width = root_lista.winfo_screenwidth()
    screen_height = root_lista.winfo_screenheight()
    window_width = 750
    window_height = 550
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root_lista.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = customtkinter.CTkLabel(master=root_lista, text="LISTA DE EMAILS", font=("Arial", 34, 'bold'),
                                   text_color='#1b98e0')
    label.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    # Criar uma planilha
    frame = customtkinter.CTkFrame(master=root_lista, fg_color='#474943', width=700, height=400)
    frame.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

    header_email = customtkinter.CTkLabel(master=frame, text="Email", font=("Arial", 14, 'bold'),
                                          text_color='#1b98e0', width=35, anchor=customtkinter.W)
    header_email.grid(row=0, column=0, padx=10, pady=5)

    header_date = customtkinter.CTkLabel(master=frame, text="Data", font=("Arial", 14, 'bold'),
                                         text_color='#1b98e0', width=35, anchor=customtkinter.W)
    header_date.grid(row=0, column=1, padx=10, pady=5)

    button_voltar = customtkinter.CTkButton(master=root_lista,
                                            width=100,
                                            height=30,
                                            border_width=0,
                                            corner_radius=8,
                                            fg_color='#4682B4',
                                            text="Voltar",
                                            font=("Nunito", 14, 'bold'),
                                            command=voltar)
    button_voltar.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)
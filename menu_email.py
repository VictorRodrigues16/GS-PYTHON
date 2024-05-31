import tkinter as tk
from tkinter import messagebox
import customtkinter
from img import img_64
from datetime import datetime
from Disparo_Email import enviar_email
from lista_emails import criar_janela_emails_lista
from lista_emails import emails_data


def validar_email(email):
    # Utilizando expressão regular para validação de e-mail
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def button_event(entry_email, root_login):
    email = entry_email.get()

    if not email:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
        return

    if not validar_email(email):
        messagebox.showwarning("Email Inválido", "Por favor, insira um endereço de email válido.")
        return

    # Salvar email na lista global com a data atual
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emails_data.append({"email": email, "date": current_date})

    enviar_email(email)
    messagebox.showinfo("Sucesso", "Email enviado com sucesso!")
    root_login.deiconify()  # Restaurar a janela de envio de e-mail

def criar_janela_email():
    root_login = customtkinter.CTkToplevel()
    root_login.title("INSIRA UM EMAIL")
    root_login.configure(fg_color='#161b33')

    screen_width = root_login.winfo_screenwidth()
    screen_height = root_login.winfo_screenheight()
    window_width = 750
    window_height = 500
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root_login.geometry(f"{window_width}x{window_height}+{x}+{y}")

    imgnew = customtkinter.CTkImage(img_64, size=(250, 210))
    label_image = customtkinter.CTkLabel(master=root_login, image=imgnew, text=' ')
    label_image.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    label = customtkinter.CTkLabel(master=root_login, text="INSIRA UM E-MAIL", font=("Arial", 34, 'bold'),
                                   text_color='#1b98e0')
    label.place(relx=0.5, rely=0.37, anchor=tk.CENTER)

    entry_email = customtkinter.CTkEntry(master=root_login,
                                         placeholder_text="E-mail",
                                         text_color='#939191',
                                         font=("Arial", 16, 'bold'),
                                         width=350,
                                         height=50,
                                         border_width=1,
                                         corner_radius=10,
                                         justify='center',
                                         fg_color='#474943')
    entry_email.place(relx=0.5, rely=0.57, anchor=tk.CENTER)

    button = customtkinter.CTkButton(master=root_login,
                                     width=210,
                                     height=42,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color='#4682B4',
                                     text="ENVIAR",
                                     font=("Nunito", 14, 'bold'),
                                     command=lambda: button_event(entry_email, root_login))
    button.place(relx=0.5, rely=0.79, anchor=tk.CENTER)

    button_show_emails = customtkinter.CTkButton(master=root_login,
                                                 width=210,
                                                 height=42,
                                                 border_width=0,
                                                 corner_radius=8,
                                                 fg_color='#4682B4',
                                                 text="MOSTRAR EMAILS",
                                                 font=("Nunito", 14, 'bold'),
                                                 command=lambda: show_email_list(root_login))
    button_show_emails.place(relx=0.5, rely=0.89, anchor=tk.CENTER)

    root_login.mainloop()

def show_email_list(root_login):
    root_login.withdraw()  # Esconder a janela de envio de e-mail
    criar_janela_emails_lista(root_login)

if __name__ == "__main__":
    criar_janela_email()

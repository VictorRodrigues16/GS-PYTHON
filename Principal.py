import tkinter as tk
from tkinter import messagebox
import customtkinter
from Cadastrar import criar_janela_cadastro
from img import img_64
import json

def validar_email(email):
    # Utilizando expressão regular para validação de e-mail
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def verificar_credenciais(email, senha):
    try:
        with open('credenciais.json', 'r') as f:
            credenciais = json.load(f)

        for usuario in credenciais:
            if usuario.get('email') == email and usuario.get('senha') == senha:
                return True
        return False
    except FileNotFoundError:
        return False
    except json.JSONDecodeError:
        return False

def toggle_password_visibility(entry_senha):
    entry_senha.show_password = not entry_senha.show_password
    if entry_senha.show_password:
        entry_senha.configure(show="")
    else:
        entry_senha.configure(show="⭐")

def button_event(entry_email, entry_senha, root_login):
    email = entry_email.get()
    senha = entry_senha.get()

    if not email or not senha:
        messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
        return

    if not validar_email(email):
        messagebox.showwarning("Email Inválido", "Por favor, insira um endereço de email válido.")
        return

    if verificar_credenciais(email, senha):
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        root_login.withdraw()
        menu_info()
    else:
        messagebox.showwarning("Credenciais Inválidas", "Email ou senha incorretos. Por favor, tente novamente.")

def criar_janela_login():
    root_login = customtkinter.CTkToplevel()
    root_login.configure(fg_color='#f1f1f1')
    root_login.title("FAÇA SEU LOGIN")
    root_login.configure(fg_color='#161b33')

    screen_width = root_login.winfo_screenwidth()
    screen_height = root_login.winfo_screenheight()
    window_width = 750
    window_height = 550
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root_login.geometry(f"{window_width}x{window_height}+{x}+{y}")

    imgnew = customtkinter.CTkImage(img_64, size=(250, 210))
    label_image = customtkinter.CTkLabel(master=root_login, image=imgnew, text=' ')
    label_image.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    label = customtkinter.CTkLabel(master=root_login, text="ACESSAR SUA CONTA", font=("Arial", 34, 'bold'),
                                   text_color='#1b98e0')
    label.place(relx=0.5, rely=0.37, anchor=tk.CENTER)

    entry_email = customtkinter.CTkEntry(master=root_login,
                                         placeholder_text="Insira seu E-mail",
                                         text_color='#939191',
                                         font=("Arial", 16, 'bold'),
                                         width=350,
                                         height=45,
                                         border_width=1,
                                         corner_radius=10,
                                         justify='center',
                                         fg_color='#474943')
    entry_email.place(relx=0.5, rely=0.53, anchor=tk.CENTER)

    entry_senha = customtkinter.CTkEntry(master=root_login,
                                         placeholder_text="Insira sua senha",
                                         text_color='#939191',
                                         font=("Arial", 16, 'bold'),
                                         width=350,
                                         height=45,
                                         border_width=1,
                                         corner_radius=10,
                                         justify='center',
                                         fg_color='#474943')
    entry_senha.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    entry_senha.show_password = False
    entry_senha.configure(show="⭐")

    button_show_password = customtkinter.CTkButton(master=root_login,
                                                   width=43,
                                                   height=33,
                                                   border_width=0,
                                                   corner_radius=0,
                                                   text="👁️",
                                                   font=("Nunito", 14, 'bold'), text_color='#3284AE',
                                                   hover_color='#2a7ca6',
                                                   fg_color='transparent',
                                                   hover=False,
                                                   command=lambda: toggle_password_visibility(entry_senha))
    button_show_password.place(relx=0.79, rely=0.65, anchor=tk.CENTER)

    button = customtkinter.CTkButton(master=root_login,
                                     width=210,
                                     height=42,
                                     border_width=0,
                                     corner_radius=8,
                                     fg_color='#4682B4',
                                     text="ENTRAR",
                                     font=("Nunito", 14, 'bold'),
                                     command=lambda: button_event(entry_email, entry_senha, root_login))
    button.place(relx=0.5, rely=0.79, anchor=tk.CENTER)

    label = customtkinter.CTkLabel(master=root_login, text="Esqueci minha senha", font=("Arial", 12, 'bold'),
                                   text_color='#676666')
    label.place(relx=0.5, rely=0.87, anchor=tk.CENTER)

    label = customtkinter.CTkLabel(master=root_login, text="Não tem uma conta?", font=("Arial", 12, 'bold'),
                                   text_color='#676666')
    label.place(relx=0.44, rely=0.91, anchor=tk.CENTER)

    button = customtkinter.CTkButton(master=root_login,
                                     width=60,
                                     height=12,
                                     border_width=0,
                                     corner_radius=0,
                                     text="Crie agora!",
                                     font=("Nunito", 12, 'bold'), text_color='#3284AE',
                                     fg_color='transparent',
                                     hover=False,
                                     command=lambda: (root_login.withdraw(), criar_janela_cadastro(root_login)))
    button.place(relx=0.57, rely=0.91, anchor=tk.CENTER)

    root_login.mainloop()

if __name__ == "__main__":
    criar_janela_login()

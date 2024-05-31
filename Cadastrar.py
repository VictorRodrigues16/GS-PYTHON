import tkinter as tk
from tkinter import messagebox
import json
import os
import customtkinter
from img import img_64

USERS_FILE = "credenciais.json"


def validar_email(email):
    """Valida o formato do e-mail."""
    try:
        return "@" in email and "." in email
    except TypeError:
        return False


def validar_nome(nome):
    """Valida se o nome contém apenas letras."""
    try:
        return all(parte.isalpha() for parte in nome.split())
    except AttributeError:
        return False


def verificar_email_existente(email):
    """Verifica se o e-mail já existe no arquivo de usuários."""
    try:
        if not os.path.exists(USERS_FILE):
            return False

        with open(USERS_FILE, "r") as file:
            usuarios = json.load(file)

        return any(usuario["email"] == email for usuario in usuarios)
    except (FileNotFoundError, json.JSONDecodeError):
        return False


def cadastrar_usuario(nome, email, senha):
    """Cadastra um novo usuário."""
    try:
        usuario = {'nome': nome, 'email': email, 'senha': senha}
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, "w") as file:     #Quando um arquivo for aberto com o with ele é fechado automaticamente.
                json.dump([usuario], file, indent=4)
        else:
            with open(USERS_FILE, "r") as file:
                usuarios = json.load(file)
            usuarios.append(usuario)
            with open(USERS_FILE, "w") as file:
                json.dump(usuarios, file, indent=4)

        print("Usuário cadastrado com sucesso:", usuario)
    except (FileNotFoundError, json.JSONDecodeError, TypeError):
        print("Erro ao cadastrar usuário.")


def criar_janela_cadastro(root):
    """Cria a janela de cadastro de usuários."""

    def button_event(entry_nome, entry_email, entry_senha, entry_senha2):
        """Evento do botão de cadastro."""
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        senha2 = entry_senha2.get()

        try:
            if not (nome and email and senha and senha2):
                messagebox.showwarning("Campos Vazios", "Por favor, preencha todos os campos.")
                return

            if not validar_nome(nome):
                messagebox.showwarning("Nome Inválido", "O nome não pode conter números ou caracteres especiais.")
                return

            if not validar_email(email):
                messagebox.showwarning("Email Inválido", "Por favor, insira um endereço de email válido.")
                return

            if verificar_email_existente(email):
                messagebox.showwarning("Email Existente", "Este email já está cadastrado. Por favor, escolha outro.")
                return

            if senha != senha2:
                messagebox.showwarning("Senhas Diferentes", "As senhas não coincidem. Por favor, verifique.")
                return

            cadastrar_usuario(nome, email, senha)
            messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
            root_cadastro.destroy()
            root.deiconify()  # Torna a janela principal visível novamente
        except Exception as e:
            print(f"Erro durante o cadastro: {e}")

    root_cadastro = customtkinter.CTkToplevel()
    root_cadastro.configure(fg_color='#161b33')
    root_cadastro.title("CRIE SUA CONTA")

    screen_width = root_cadastro.winfo_screenwidth()
    screen_height = root_cadastro.winfo_screenheight()
    window_width = 800
    window_height = 600
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root_cadastro.geometry(f"{window_width}x{window_height}+{x}+{y}")

    imgnew = customtkinter.CTkImage(img_64, size=(250, 210))
    label_image = customtkinter.CTkLabel(master=root_cadastro, image=imgnew, text=' ')
    label_image.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    label = customtkinter.CTkLabel(master=root_cadastro, text="CRIE SUA CONTA", font=("Arial", 34, 'bold'),
                                   text_color='#3284AE')
    label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    entry_nome = customtkinter.CTkEntry(master=root_cadastro, placeholder_text="Nome Completo", text_color='#939191',
                                        font=("Arial", 16, 'bold'), width=350, height=45, border_width=1,
                                        corner_radius=10, justify='center', fg_color='#474943')
    entry_nome.place(relx=0.5, rely=0.44, anchor=tk.CENTER)

    entry_email = customtkinter.CTkEntry(master=root_cadastro, placeholder_text="Insira seu melhor E-mail",
                                         text_color='#939191', font=("Arial", 16, 'bold'), width=350, height=45,
                                         border_width=1, corner_radius=10, justify='center', fg_color='#474943')
    entry_email.place(relx=0.5, rely=0.54, anchor=tk.CENTER)

    entry_senha = customtkinter.CTkEntry(master=root_cadastro, placeholder_text="Insira sua senha",
                                         text_color='#939191',
                                         font=("Arial", 16, 'bold'), width=350, height=45, border_width=1,
                                         corner_radius=10, justify='center', fg_color='#474943')
    entry_senha.place(relx=0.5, rely=0.64, anchor=tk.CENTER)

    entry_senha2 = customtkinter.CTkEntry(master=root_cadastro, placeholder_text="Confirme sua senha",
                                          text_color='#939191',
                                          font=("Arial", 16, 'bold'), width=350, height=45, border_width=1,
                                          corner_radius=10, justify='center', fg_color='#474943')
    entry_senha2.place(relx=0.5, rely=0.74, anchor=tk.CENTER)

    button = customtkinter.CTkButton(master=root_cadastro, width=210, height=42, border_width=0, corner_radius=8,
                                     text="CADASTRAR", font=("Nunito", 14, 'bold'), fg_color='#4682B4',
                                     command=lambda: button_event(entry_nome, entry_email, entry_senha, entry_senha2))
    button.place(relx=0.5, rely=0.87, anchor=tk.CENTER)

    root_cadastro.mainloop()


if __name__ == "__main__":
    root = customtkinter.CTk()
    criar_janela_cadastro(root)

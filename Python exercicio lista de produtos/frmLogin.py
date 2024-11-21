import tkinter as tk
from tkinter import messagebox
import sqlite3
import frmMenu

conn = sqlite3.connect('./db_myapp_1.db')
cursor = conn.cursor()
txtLogin = None
txtSenha = None
janela = None

def realizarLogin():
    usuario = txtLogin.get()
    senha = txtSenha.get()

    try:
        cursor.execute("SELECT * FROM Usuario WHERE login = ? and senha = ?", (usuario, senha))
        listaUsuario = cursor.fetchall()
        
        if len(listaUsuario) > 0:
            janela.destroy()
            frmMenu.iniciarJanela()
        else:
            messagebox.showwarning("Não encontrou","Ops! Usuário ou senha inválidos")
    except:
        messagebox.showerror('Erro de conexão com a base', "Erro ao buscar os dados na base de dados")

def iniciarJanela():
    global txtLogin, txtSenha, janela
    janela = tk.Tk()
    janela.geometry("300x300")
    janela.title("Tela de Login")

    lblLogin = tk.Label(janela, text="Login")
    lblLogin.pack()
    txtLogin = tk.Entry(janela)
    txtLogin.pack()

    lblSenha = tk.Label(janela, text="Senha")
    lblSenha.pack()
    txtSenha = tk.Entry(janela)
    txtSenha.config(show="*")
    txtSenha.pack()

    btnLogin = tk.Button(janela, text="Login", command=realizarLogin)
    btnLogin.pack()
    
    janela.mainloop()   

if __name__ =="__main__":
    iniciarJanela()
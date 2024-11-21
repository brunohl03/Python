import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('./db_myapp_1.db')
cursor = conn.cursor()
janela = None
tabela = None

def listaProdutos():
    try:
        cursor.execute("SELECT * FROM Produto")
        listaProduto = cursor.fetchall()
            
        for produto in listaProduto:
            tabela.insert("", tk.END, values=produto)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao buscar os dados na base de dados: {e}")

def iniciarJanela():
    global janela, tabela

    janela = tk.Tk()
    janela.title("Cadastro de produtos")
    janela.geometry("900x400")  

    tabela = ttk.Treeview(janela, columns=("ID", "Nome", "Categoria", "Descrição", "Preço Custo", "Preço Venda", "Quantidade"), show="headings")

    tabela.heading("ID", text="ID")
    tabela.heading("Nome", text="Nome")
    tabela.heading("Categoria", text="Categoria")
    tabela.heading("Descrição", text="Descrição")
    tabela.heading("Preço Custo", text="Preço Custo")
    tabela.heading("Preço Venda", text="Preço Venda")
    tabela.heading("Quantidade", text="Quantidade")

    tabela.column("ID", width=50, anchor="center")
    tabela.column("Nome", width=150, anchor="center")
    tabela.column("Categoria", width=100, anchor="center")
    tabela.column("Descrição", width=200, anchor="center")
    tabela.column("Preço Custo", width=100, anchor="center")
    tabela.column("Preço Venda", width=100, anchor="center")
    tabela.column("Quantidade", width=100, anchor="center")

    tabela.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    listaProdutos()

    btn_fechar = tk.Button(janela, text="Fechar", command=janela.quit)
    btn_fechar.pack(pady=10)
    janela.mainloop()

if __name__ == "__main__":
    iniciarJanela()

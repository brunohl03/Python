import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('./db_myapp_1.db')
cursor = conn.cursor()

janela = None
txtNome = None
txtCategoria = None
txtDescricao = None
txtPrecoCusto = None
txtPrecoVenda = None
txtQuantidade = None

def salvarProduto():
    try:
        if txtNome.get() != "" and txtCategoria.get() != "" and txtPrecoCusto.get() != "" and txtPrecoVenda.get() != "" and txtQuantidade.get() != "":
            nome = txtNome.get()
            categoria = txtCategoria.get()
            descricao = txtDescricao.get()
            precoCusto = float(txtPrecoCusto.get())
            precoVenda = float(txtPrecoVenda.get())
            quantidade = int(txtQuantidade.get())

            cursor.execute("INSERT INTO Produto(nome, categoria, descricao, precoCusto, precoVenda, quantidade) values(?,?,?,?,?,?)", (nome, categoria, descricao, precoCusto, precoVenda, quantidade))
            conn.commit()
            messagebox.showinfo("Sucesso", "Produto inserido com sucesso")
            janela.destroy()
        else:
            messagebox.showwarning("Preencha os campos", "Você precisa preencher os campos Obrigatórios!")
    except:
        messagebox.showerror("Erro", "Erro ao salvar os dados na base de dados")

def iniciarJanela():
    global janela, txtNome, txtCategoria, txtDescricao,txtPrecoCusto, txtPrecoVenda, txtQuantidade
    janela = tk.Tk()
    janela.title("Cadastro de produtos")
    janela.geometry("300x400")

    lblNome = tk.Label(janela, text="Nome")
    lblNome.pack()
    txtNome = tk.Entry(janela)
    txtNome.pack()

    lblCategoria = tk.Label(janela, text="Categoria")
    lblCategoria.pack()
    txtCategoria = tk.Entry(janela)
    txtCategoria.pack()

    lblDescricao= tk.Label(janela, text="Descrição")
    lblDescricao.pack()
    txtDescricao = tk.Entry(janela)
    txtDescricao.pack()

    lblPrecoCusto= tk.Label(janela, text="Preço Custo")
    lblPrecoCusto.pack()
    txtPrecoCusto = tk.Entry(janela)
    txtPrecoCusto.pack()

    lblPrecoVenda= tk.Label(janela, text="Preço Venda")
    lblPrecoVenda.pack()
    txtPrecoVenda = tk.Entry(janela)
    txtPrecoVenda.pack()

    lblQuantidade = tk.Label(janela, text="Quantidade")
    lblQuantidade.pack()
    txtQuantidade = tk.Entry(janela)
    txtQuantidade.pack()

    btnCadastrar = tk.Button(janela, text="Cadastrar", command=salvarProduto)
    btnCadastrar.pack()

    janela.mainloop()

if __name__ == "__main__":
    iniciarJanela()
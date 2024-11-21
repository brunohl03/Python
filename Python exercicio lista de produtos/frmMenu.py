import tkinter as tk
import frmProdutoCadastro
import frmProdutoLista

def iniciarJanela():
    janela = tk.Tk()
    janela.title("Tela de Menu")
    janela.geometry("300x400")

    btnCadastrarProduto = tk.Button(janela, 
                                    text="Cadastrar Produtos",
                                    command=frmProdutoCadastro.iniciarJanela
                                    )
    btnCadastrarProduto.pack()

    btnCadastrarProduto = tk.Button(janela, 
                                    text="Lista de Produtos",
                                    command=frmProdutoLista.iniciarJanela
                                    )
    btnCadastrarProduto.pack()

    janela.mainloop()

if __name__ == "__main__":
    iniciarJanela()
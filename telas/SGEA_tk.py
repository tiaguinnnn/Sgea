from tkinter import *
from telas.atualizar_produto import SgeaTkAtualizar
from telas.registrartela import SgeaTkRegistro
from data.db import pesquisar_produto

class SGEATk:
    def __init__(self, janela):
        produtos = pesquisar_produto()
        self.janela = janela
        janela.geometry('900x600')
        janela.title("SGEA")
        janela.config(background="#B8CAD4")

       
        Label(janela, text="Menu SGEA", font=("Arial", 22, "bold"), bg="#B8CAD4", fg="black").grid(row=0, column=0, pady=20)

      
        Button(janela, text="Registrar Produto", command=self.abrir_registro, padx=100, pady=15, font=("Arial", 15)).grid(row=1, column=0, pady=10)
        Button(janela, text="Atualizar Produto", command=self.abrir_atualizar, pady=15, padx=100, font=("Arial", 15)).grid(row=2, column=0, pady=10)

      
        frame_lista = Frame(janela)
        frame_lista.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")

        
        janela.grid_rowconfigure(3, weight=1)
        janela.grid_columnconfigure(0, weight=1)

        frame_lista.grid_rowconfigure(0, weight=1)
        frame_lista.grid_columnconfigure(0, weight=1)

       
        self.lista_produtos = Listbox(frame_lista, font=("Arial", 12))
        self.lista_produtos.grid(row=0, column=0, sticky="nsew")

        scrollbar = Scrollbar(frame_lista, orient=VERTICAL, command=self.lista_produtos.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.lista_produtos.config(yscrollcommand=scrollbar.set)

       
        for i in produtos:
            self.lista_produtos.insert(END, i)

    def abrir_registro(self):
        nova_janela = Toplevel(self.janela)
        SgeaTkRegistro(nova_janela)

    def abrir_atualizar(self):
        produtos = pesquisar_produto()
        nova_janela = Toplevel(self.janela)
        SgeaTkAtualizar(nova_janela, produtos)

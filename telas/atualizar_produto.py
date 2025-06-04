from tkinter import *
from data.db import pesquisar_produto
from services.atualizar_produto_def import atualizar_produto

class SgeaTkAtualizar:
    def __init__(self, janela, produtos):
        self.janela = janela
        janela.title('Atualizar Estoque')
        janela.geometry('500x500')
        janela.config(bg='#B8CAD4')

        Label(janela, text='Atualizar Produtos:', font=('Arial', 16, 'bold'), bg='yellow')\
            .place(relx=0.5, rely=0.03, anchor='n')

        self.lista_estoque = Listbox(janela, font=('Arial', 12, 'bold'))
        self.lista_estoque.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.25)

        for i in produtos:
            self.lista_estoque.insert(END, i)

        Label(janela, text="Produto a Atualizar:", font=('Arial', 12, 'bold')).place(relx=0.1, rely=0.4, relwidth=0.35)
        self.ent_produto = Entry(janela)
        self.ent_produto.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.04)

        Label(janela, text="Adicionar Quantidade:", font=('Arial', 12, 'bold')).place(relx=0.1, rely=0.5, relwidth=0.35)
        self.ent_adicionar = Entry(janela)
        self.ent_adicionar.place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.04)

        Label(janela, text="Remover Quantidade:", font=('Arial', 12, 'bold')).place(relx=0.1, rely=0.6, relwidth=0.35)
        self.ent_remover = Entry(janela)
        self.ent_remover.place(relx=0.5, rely=0.6, relwidth=0.4, relheight=0.04)

        Button(janela, text="Atualizar", command=self.atualizar_produto)\
            .place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.07)

        Button(janela, text="Fechar", command=janela.destroy)\
            .place(relx=0.3, rely=0.85, relwidth=0.4, relheight=0.07)

    def atualizar_produto(self):
        produto = self.ent_produto.get()
        adicionar = self.ent_adicionar.get()
        remover = self.ent_remover.get()
        atualizar_produto(produto, adicionar, remover)
        print(f"Atualizar produto: {produto}, +{adicionar}, -{remover}")

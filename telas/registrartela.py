from tkinter import *
from services.registrar import registrar_produto

class SgeaTkRegistro:
    def __init__(self, janela):
        self.janela = janela
        janela.title('Registrar Produto')
        janela.geometry('500x500')
        janela.config(bg='#B8CAD4')

        Label(janela, text='Registrar Novos Produtos:', font=('Arial', 16, 'bold'), bg='yellow').place(relx=0.5, rely=0.05, anchor='n')

        self.ent_nome = Entry(janela)
        self.ent_categoria = Entry(janela)
        self.ent_qtd = Entry(janela)
        self.ent_preco = Entry(janela)
        self.ent_validade = Entry(janela)
        self.ent_localidade = Entry(janela)

        Label(janela, text="Nome Produto:", font=("Arial", 10, 'bold')).place(relx=0.2, rely=0.15, relwidth=0.25)
        self.ent_nome.place(relx=0.5, rely=0.15, relwidth=0.4)

        Label(janela, text="Categoria Produto:", font=("Arial", 10, 'bold')).place(relx=0.2, rely=0.25, relwidth=0.25)
        self.ent_categoria.place(relx=0.5, rely=0.25, relwidth=0.4)

        Label(janela, text="Preço Produto:", font=("Arial", 10, 'bold')).place(relx=0.2, rely=0.35, relwidth=0.25)
        self.ent_preco.place(relx=0.5, rely=0.35, relwidth=0.4)

        Label(janela, text="Data de Validade:", font=("Arial", 10, 'bold')).place(relx=0.2, rely=0.45, relwidth=0.25)
        self.ent_validade.place(relx=0.5, rely=0.45, relwidth=0.4)

        Label(janela, text="Localidade:", font=("Arial", 10, 'bold')).place(relx=0.2, rely=0.55, relwidth=0.25)
        self.ent_localidade.place(relx=0.5, rely=0.55, relwidth=0.4)

        Button(janela, text="Registrar", command=self.registrar_produto_tela).place(relx=0.4, rely=0.7, relwidth=0.2)

    def registrar_produto_tela(self):
        nome = self.ent_nome.get()
        categoria = self.ent_categoria.get()
        preco = self.ent_preco.get()
        validade = self.ent_validade.get()
        localidade = self.ent_localidade.get()
        registrar_produto(nome, categoria, preco, validade, localidade)
        print(f"Produto registrado: {nome}, {categoria}, {preco}, {validade}, {localidade}")
        self.janela.destroy()

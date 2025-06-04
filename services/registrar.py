from tkinter import *
from data.db import inserir_produtos

estoque = []
def registrar_produto(nome_produto, categoria, preco, validade, localidade):
    if(nome_produto, categoria, preco, validade, localidade):
        inserir_produtos(nome_produto, categoria, preco, validade, localidade)
    else:
        print('erro ao registrar produto')
    
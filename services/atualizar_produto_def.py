from tkinter import *
from data.db import adicionar_produtos
from data.db import remover_produtos

def atualizar_produto(produto, adicionar, remover):
    if(produto and adicionar):
        adicionar_produtos(produto,adicionar)
    elif(produto and remover):
        remover_produtos(produto,remover)

    

        
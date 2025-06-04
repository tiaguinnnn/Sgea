from tkinter import *
from tkinter import messagebox
from telas.SGEA_tk import SGEATk
from data.db  import buscar_usuario

class Usuario:
    def __init__(self):
        self.__nome = "admim"
        self.__senha = "sgea2025"

    def verificar(self, janela, senha, nome):
        resultado = buscar_usuario(nome, senha)
        print(resultado)
        if(resultado[1] == self.__senha and resultado[0] == self.__nome ):
            messagebox.showinfo("Verificado", "Você digitou a senha correta Bem-Vindo Usuario ")
            janela.destroy()
            janela = Tk()
            app = SGEATk(janela)
            janela.mainloop()
                                
        else:
            messagebox.showerror("ERRO", "Você digitou a senha errada")
        
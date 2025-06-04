from tkinter import *
from models.usuario import Usuario
 
class Login:
    def __init__(self, janela):
        self.janela = janela
        janela.geometry('900x600')
        janela.config(bg='#B8CAD4')

        label_titulo = Label(janela, text="Login", font=("Arial", 22, "bold"), bg="#B8CAD4", fg="black").grid(row=0, column=0 ,pady=5)
        label_usuario = Label(janela, text="Usuário:")
        label_usuario.grid(row=1, column=0 ,pady=5)
        self.entry_usuario = Entry(janela)
        self.entry_usuario.grid(row=2, column=0 ,pady=5)
        
        label_senha = Label(janela, text="Senha:")
        label_senha.grid(row=3, column=0 ,pady=5)
        self.entry_senha = Entry(janela, show="")
        self.entry_senha.grid(row=4, column=0 ,pady=5)
        
        botao_login = Button(janela, text="Login", command=self.verificar_dados)
        botao_login.grid(row=5, column=0 ,pady=10)

        janela.grid_columnconfigure(0, weight = 1 )

    def verificar_dados(self):
        senha = self.entry_senha.get()
        usuario = self.entry_usuario.get()
        user = Usuario()
        user.verificar(self.janela,senha,usuario)
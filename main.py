from tkinter import * 
from telas.login import Login
from data.db import inserir_usuario
from telas.SGEA_tk import SGEATk

if __name__ == '__main__':
    inserir_usuario()
    janela = Tk()
    app = Login(janela)
    janela.mainloop()

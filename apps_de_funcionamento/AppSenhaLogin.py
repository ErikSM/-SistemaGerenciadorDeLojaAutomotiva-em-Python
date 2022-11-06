import time
import tkinter

from apps_de_funcionamento.AppLojaAberta import AppLojaAberta
from estrutura.AppSenha import AppSenha
from estrutura.Loja import Loja


def abrir_loja(loja: Loja):
    AppLojaAberta(loja).window.mainloop()


class AppSenhaLogin(AppSenha):

    def __init__(self, title, loja: Loja):
        super().__init__(title)

        self.__loja = loja

        self.__senha_da_loja = loja.senha
        self.__senha_digitada = None

        self.botao_adicionar.config(text="  Logar...", command=self.validar_senha)

        self.texto_relatorio.config(state=tkinter.NORMAL)
        self.texto_relatorio.insert(1.0, "\n   Digite a senha no campo acima!!")
        self.texto_relatorio.config(state=tkinter.DISABLED)

    def validar_senha(self):
        self.__senha_digitada = self.captura_senha.get()
        if self.__senha_digitada == self.__senha_da_loja:
            time.sleep(1.0)
            self.window.destroy()
            abrir_loja(self.__loja)
        else:
            self.texto_relatorio.config(state=tkinter.NORMAL)
            self.texto_relatorio.delete(1.0, "end")
            self.texto_relatorio.insert(1.0, "\n   Falha ao tentar logar!!    ")
            self.texto_relatorio.insert(1.0, "\n   tente novamente...!!")
            self.texto_relatorio.config(state=tkinter.DISABLED)

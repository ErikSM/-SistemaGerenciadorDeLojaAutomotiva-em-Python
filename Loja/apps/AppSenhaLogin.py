import time
import tkinter

from apps.AppLojaAberta import AppLojaAberta
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

        self.frame_dados.pack(fill="both", side="top")

        self.botao_executar.config(text="  Logar...", command=self.validar_senha)
        self.botao_executar.grid(row=0, column=2)

        self.label.grid(row=0, column=0)
        self.captura_senha.grid(row=0, column=1)

        self.texto_relatorio.pack(fill="both", side="bottom")
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

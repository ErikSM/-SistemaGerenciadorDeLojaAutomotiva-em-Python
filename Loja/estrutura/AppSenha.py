import tkinter

from estrutura.AppBase import AppBase


class AppSenha(AppBase):
    def __init__(self, title):
        super().__init__(title)

        self.window.geometry("+700+300")

        self.frame_dados.config(bg="grey40")

        self.texto_relatorio.config(font=("Consolas", 9), width=30, height=4,
                                    fg='white', state=tkinter.DISABLED)

        self.botao_executar.config(text=" ", bd=3, command=None)

        self.label = tkinter.Label(self.frame_dados, font=("arial", 9, "bold"),
                                   text="Digite a senha:", bg="grey55", bd=5)

        self.captura_senha = tkinter.Entry(self.frame_dados, bd=5)

    def _sair(self):
        self.window.quit()

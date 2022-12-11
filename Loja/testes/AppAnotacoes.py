import tkinter

from estrutura.AppBase import AppBase


class Anotacoes(AppBase):

    def __init__(self, title):
        super().__init__(title)

        self.anotacoes_para_adicionar = None

        self.window.geometry("+500+100")

        self.botao_adicionar.config(text="Adicionar anotacao")
        self.texto_relatorio.config(bg="white", fg="black", bd=1)

        self.label_anotacoes = tkinter.Label(self.window, font=('Arial', 11),
                                             text="Anotacoes:", background='white', foreground='black')
        self.label_anotacoes.pack(side="left")

        self.retornar_data_e_hora()

        self.window.mainloop()

    def criar_relatorio(self):
        self.anotacoes_para_adicionar = self.texto_relatorio.get(1.0, "end")
        print(self.anotacoes_para_adicionar)

    def salvar_anotacoes_em_texto(self):
        endereco_do_arquivo = "anotacoes/"


Anotacoes("Anotacoes")

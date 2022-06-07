import tkinter

from abc import ABCMeta


class AppBase(metaclass=ABCMeta):

    def __init__(self, title):
        # \\\ APP
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.config(bg="white", bd=12)
        self.window.resizable(0, 0)

        # \\\ Criando frame dos dados
        self.frame_dados = tkinter.Frame(self.window, bg="white", bd=4)
        self.frame_dados.pack(fill="both", side="top")

        #  \\\ criando relatorio
        self.texto_relatorio = tkinter.Text(self.window, font=("Consolas", 12), bg="black", fg="white", bd=12)
        self.texto_relatorio.config(width=70, height=10)
        self.texto_relatorio.pack(fill="both", side="bottom")
        self.texto_relatorio.config(state=tkinter.DISABLED)

        # \ criando botao
        self.botao_adicionar = tkinter.Button(self.frame_dados, text="Registrar", bg="grey")
        self.botao_adicionar.config(command=self.criar_relatorio)
        self.botao_adicionar.grid(row=0, column=1)

    def criar_relatorio(self):
        pass

    def _apagar_relatorio(self):
        self.texto_relatorio.delete(1.0, "end")

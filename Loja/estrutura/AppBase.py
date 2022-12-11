import tkinter

from abc import ABCMeta
from time import strftime


class AppBase(metaclass=ABCMeta):

    def __init__(self, title):
        # APP
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.config(bg="white", bd=12)
        self.window.resizable(False, False)
        self.window.geometry("+500+200")

        # frame
        self.frame_dados = tkinter.Frame(self.window, bg="white", bd=4)
        self.frame_dados.pack(fill="both", side="top")

        # relatorio
        self.texto_relatorio = tkinter.Text(self.window, font=("Consolas", 12), bg="black", fg="white", bd=12)
        self.texto_relatorio.config(width=40, height=10)
        self.texto_relatorio.config(state=tkinter.NORMAL)
        self.texto_relatorio.pack(fill="both", side="bottom")

        self.label_calendario = tkinter.Label(self.window, font=('calibri', 10), background='grey90',
                                              foreground='black')
        self.label_calendario.pack(side="right")

        # botao
        self.botao_adicionar = tkinter.Button(self.frame_dados, text="Registrar", bg="grey")
        self.botao_adicionar.config(command=self.criar_relatorio)
        self.botao_adicionar.grid(row=0, column=1)

    def criar_relatorio(self):
        pass

    def _apagar_relatorio(self):
        self.texto_relatorio.delete(1.0, "end")

    # -------------  teste --------------------------
    def retornar_data_e_hora(self):
        string_data = strftime('%d/%m/%Y')
        string_hora = strftime('%H:%M:%S')
        self.label_calendario.config(text=f'{string_data}{" " * 7}{string_hora}')
        self.label_calendario.after(1000, self.retornar_data_e_hora)
    # ------------------------------------------------

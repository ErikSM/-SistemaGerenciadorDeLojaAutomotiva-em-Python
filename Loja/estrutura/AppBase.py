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

        # frames
        self.frame_dados = tkinter.Frame(self.window, bg="white", bd=4)

        self.frame_dados_2 = tkinter.Frame(self.window, bg="white", bd=4)

        # botao
        self.botao_executar = tkinter.Button(self.frame_dados, text="Registrar", bg="grey",
                                             command=self.criar_relatorio)

        # data e hora
        self.label_calendario = tkinter.Label(self.frame_dados_2, font=('calibri', 10), background='grey90',
                                              foreground='black')

        # relatorio
        self.texto_relatorio = tkinter.Text(self.window, font=("Consolas", 12), bg="black", fg="white", bd=12, width=40,
                                            height=10, state=tkinter.NORMAL)

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

import tkinter

from apps_de_funcionamento.AppSenhaLogin import AppSenhaLogin
from entrada_de_dados.lista_de_lojas_criadas import lojas_registradas
from apps_de_funcionamento.AppLojaAberta import abrir_registro_de_loja, AppLojaAberta


def start():
    AppLojaStart("Crie ou Abra um loja para iniciar")


def exibir_loja_selecionada(loja_select):
    loja = loja_select
    if loja.senha == None:
        return AppLojaAberta(loja_select).window.mainloop()
    else:
        return AppSenhaLogin("Login", loja_select)


class AppLojaStart():
    def __init__(self, title):

        self.opcoes_de_loja = None

        # \\\_ APP
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.config(bg="white", bd=30)
        self.window.minsize(width=500, height=100)
        self.window.resizable(0, 0)

        # \ Criando menu
        self.menu_principal = tkinter.Menu(self.window)

        # \\ Menu loja
        self.menu_loja = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_loja.add_command(label="Registrar Nova Loja", command=abrir_registro_de_loja)
        self.menu_loja.add_command(label="Abrir Loja Existente", command=self.abrir_opcoes_de_loja)
        self.menu_principal.add_cascade(label="Loja", menu=self.menu_loja)
        self.window.config(menu=self.menu_principal)

        # Editando e criando segundo frame
        self.frame = tkinter.Frame(self.window, bg="grey60")
        self.frame.pack(side="top")
        self.frame_2 = tkinter.Frame(self.window, bg="grey60")
        self.frame_2.pack(side="bottom")

        # Mensagem de orientacao para o usuario
        self.texto_mensagem = tkinter.Label(self.frame, font="Consolas 11 bold", bg="white")
        self.texto_mensagem.config(text="Nenhuma Loja Aberta no Momento...")
        self.texto_mensagem.pack()

        self.window.mainloop()

    def abrir_opcoes_de_loja(self):
        self.texto_mensagem.config(text="Selecione uma das opcoes de loja para abri-la:")

        if self.opcoes_de_loja == None:
            for i in lojas_registradas:
                self.opcoes_de_loja = tkinter.Button(self.frame_2, text=f'{i.mostrar_sem_pular_linha()}', width=50,
                                                     height=2, bg="grey")
                self.opcoes_de_loja.config(command=lambda loja_select=i: exibir_loja_selecionada(loja_select))
                self.opcoes_de_loja.pack()

        else:
            self.opcoes_de_loja == None

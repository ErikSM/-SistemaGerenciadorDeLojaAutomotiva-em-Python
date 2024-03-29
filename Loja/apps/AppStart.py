import tkinter

from apps.AppSenhaLogin import AppSenhaLogin
from entrada_de_dados.lista_lojas import lojas_registradas
from apps.AppPrincipal import abrir_registro_de_loja, AppPrincipal


def start():
    AppStart("Crie ou Abra um loja para iniciar").window.mainloop()


class AppStart:
    def __init__(self, title):

        self.opcoes_de_loja = None
        self.mostrar_opcoes = True

        # App
        self.window = tkinter.Tk()
        self.window.title(title)
        self.window.config(bg="white", bd=30)
        self.window.minsize(width=500, height=100)
        self.window.resizable(False, False)
        self.window.geometry("200x100+500+300")

        # \ Menu
        self.menu_principal = tkinter.Menu(self.window)
        self.window.config(menu=self.menu_principal)

        self.menu_loja = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Loja", menu=self.menu_loja)

        self.menu_loja.add_command(label="Abrir Loja Existente", command=self.abrir_opcoes_de_loja)
        if len(lojas_registradas) <= 2:
            self.menu_loja.add_command(label="Registrar Nova Loja", command=abrir_registro_de_loja)

        # Frame
        self.frame = tkinter.Frame(self.window, bg="grey60")
        self.frame.pack(side="top")
        self.frame_2 = tkinter.Frame(self.window, bg="grey60")
        self.frame_2.pack(side="bottom")

        # Msg
        self.texto_mensagem = tkinter.Label(self.frame, font="Consolas 11 bold", bg="white")
        self.texto_mensagem.config(text="Selecione a Loja abrindo o menu acima \nou registre uma nova loja...")
        self.texto_mensagem.pack()

    def abrir_opcoes_de_loja(self):

        self.window.geometry("")
        self.texto_mensagem.config(text="Loja(s) Registrada(s):")

        mostrar_opcoes: bool

        if len(lojas_registradas) == 0:
            self.texto_mensagem.config(text="Nenhuma loja registrada no momento...")
            mostrar_opcoes = False

        elif len(lojas_registradas) >= 3:
            self.texto_mensagem.config(text="(Limite atingido)\n"
                                            "Voce pode registrar no maximo tres lojas...\n"
                                            "Loja(s) Registrada(s):")
            mostrar_opcoes = True

        else:
            mostrar_opcoes = True

        if mostrar_opcoes:
            for i in lojas_registradas:
                self.opcoes_de_loja = tkinter.Button(self.frame_2, text=f'{i.mostrar_dados()}',
                                                     width=50, bg="grey")
                self.opcoes_de_loja.config(command=lambda loja_select=i: self._exibir_loja_selecionada(loja_select))
                self.opcoes_de_loja.pack()

    def _exibir_loja_selecionada(self, loja_select):

        self.window.destroy()
        loja = loja_select

        if loja.senha is None:
            AppPrincipal(loja_select).window.mainloop()
        else:
            AppSenhaLogin("Login", loja_select)

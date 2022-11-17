import tkinter

from entrada_de_dados.editar_lista_carros_registrados import salvar_carro_em_lista_do_main
from entrada_de_dados.gerador_de_codigo import criar_codigo_unico
from entrada_de_dados.lista_de_carros_registrados import codigos_de_carros_existentes
from estrutura.AppBase import AppBase
from estrutura.Carro import Carro


class AppCriarCarro(AppBase):

    def __init__(self, title):
        super().__init__(title)

        self.texto_temporario = tkinter.Text()
        self.carro = None
        self.mensagem_do_relatorio = None

        # Montadora
        texto_montadora = tkinter.StringVar()
        texto_montadora.set("Montadora")

        self.label_montadora = tkinter.Label(self.frame_dados, font="Arial 10",
                                             bg="white", text="Montadora:  ")

        self.entrada_montadora = tkinter.Entry(self.frame_dados, font="Arial 8 bold",
                                               bg="white", fg="black", bd=2, width=30)
        self.entrada_montadora.config(textvariable=texto_montadora)

        self.label_montadora.grid(row=1, column=1)
        self.entrada_montadora.grid(row=1, column=2)

        # Nome do Carro

        texto_nome = tkinter.StringVar()
        texto_nome.set("Nome do veiculo ")

        self.label_nome = tkinter.Label(self.frame_dados, font="Arial 10",
                                        bg="white", text="Nome:  ")

        self.entrada_do_nome = tkinter.Entry(self.frame_dados, font="Arial 8 bold",
                                             bg="white", fg="black", bd=2, width=30)
        self.entrada_do_nome.config(textvariable=texto_nome)

        self.label_nome.grid(row=2, column=1)
        self.entrada_do_nome.grid(row=2, column=2)

        # Ano
        texto_ano = tkinter.StringVar()
        texto_ano.set("ano de fabricacao")

        self.label_ano = tkinter.Label(self.frame_dados, font="Arial 10",
                                       bg="white", text="Ano:  ")

        self.entrada_ano = tkinter.Entry(self.frame_dados, font="Arial 8 bold",
                                         bg="white", fg="black", bd=2, width=30)
        self.entrada_ano.config(textvariable=texto_ano)

        self.label_ano.grid(row=3, column=1)
        self.entrada_ano.grid(row=3, column=2)

        # Preco
        texto_preco = tkinter.StringVar()
        texto_preco.set("preco do veiculo")

        self.label_preco = tkinter.Label(self.frame_dados, font="Arial 10",
                                         bg="white", text="Preco:  ")

        self.entrada_preco = tkinter.Entry(self.frame_dados, font="Arial 8 bold",
                                           bg="white", fg="black", bd=2, width=30)
        self.entrada_preco.config(textvariable=texto_preco)

        self.label_preco.grid(row=4, column=1)
        self.entrada_preco.grid(row=4, column=2)

    def criar_relatorio(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()

        self._criar_carro()

        self.texto_relatorio.insert(1.0, self.mensagem_do_relatorio)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def _criar_carro(self):
        montadora = self.entrada_montadora.get()
        nome = self.entrada_do_nome.get()
        ano = self.entrada_ano.get()
        preco = self.entrada_preco.get()
        codigo = criar_codigo_unico(codigos_de_carros_existentes)

        carro = Carro(montadora, nome, ano, preco, codigo)

        salvar_carro_em_lista_do_main(carro)

        self.carro = carro
        self.mensagem_do_relatorio = self.carro.mostrar_dados_do_veiculo()

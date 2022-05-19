import tkinter

from estrutura.AppBase import AppBase

from estrutura.Carro import Carro


class AppCarro(AppBase):

    def __init__(self, title):
        super().__init__(title)

        self.texto_temporario = tkinter.Text()
        self.carro = None

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

        self.window.mainloop()

    def criar_relatorio(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)
        self._apagar_relatorio()

        self._criar_carro()

        self.texto_relatorio.insert(1.0, self.carro)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def _criar_carro(self):
        montadora = self.entrada_montadora.get()
        nome = self.entrada_do_nome.get()
        ano = self.entrada_ano.get()
        preco = self.entrada_preco.get()

        carro = Carro(montadora, nome, ano, preco)
        self.carro = carro

        self._adicionar_em_lista_do_main(carro.montadora, carro.nome, carro.ano, carro.preco)

    def _adicionar_em_lista_do_main(self, primeira_variavel, segunda_variavel, terceira_variavel, quarta_variavel):
        super()._adicionar_em_lista_do_main(primeira_variavel, segunda_variavel, terceira_variavel, quarta_variavel)
        file = open("../entrada_de_dados/lista_de_carros_registrados.py", "r")
        texto_lido = file.read()
        self.texto_temporario.insert(1.0, texto_lido)

        self.texto_temporario.insert("end", f"\n"
                                            f'montadora = "{primeira_variavel}"\n'
                                            f'nome = "{self.segunda_variavel_sem_espaco}"\n'
                                            f'ano = "{self.terceira_variavel_sem_espaco}"\n'
                                            f'preco = "{self.quarta_variavel_sem_espaco}"'
                                            f'\n'
                                            f'carro_{self.primeira_variavel_sem_espaco}_'
                                            f'{self.segunda_variavel_sem_espaco} = Carro(montadora, nome, ano, preco)\n' 
                                            f'add_carro_na_lista_do_main(carro_{self.primeira_variavel_sem_espaco}_'
                                            f'{self.segunda_variavel_sem_espaco}, variavel_contador_de_posicao_na_lista)\n'
                                            f'variavel_contador_de_posicao_na_lista += 1'
                                            f'\n'
                                     )

        texto_reescrito = self.texto_temporario.get(1.0, "end")
        self.texto_temporario.delete(1.0, "end")
        file = open("../entrada_de_dados/lista_de_carros_registrados.py", "w")
        file.write(texto_reescrito)
        file.close()

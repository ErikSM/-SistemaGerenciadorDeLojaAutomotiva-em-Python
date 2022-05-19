import tkinter

from entrada_de_dados.criar_e_adicionar_lojas_em_lista import salvar_loja_em_lista_do_main
from estrutura.AppBase import AppBase
from estrutura.Loja import Loja


class AppCriarLoja(AppBase):

    def __init__(self, title):
        super().__init__(title)

        self.texto_temporario = tkinter.Text()
        self.loja = None

        # LOJA
        texto_no_nome = tkinter.StringVar()
        texto_no_nome.set("Loja")

        self.label_nome = tkinter.Label(self.frame_dados, font="Arial 10",
                                        bg="white", text="Loja:  ")

        self.entrada_do_nome = tkinter.Entry(self.frame_dados, font="Arial 8 bold",
                                             bg="white", fg="black", bd=2, width=30)
        self.entrada_do_nome.config(textvariable=texto_no_nome)

        self.label_nome.grid(row=1, column=1)
        self.entrada_do_nome.grid(row=1, column=2)

        # CNPJ
        texto_no_cnpj = tkinter.StringVar()
        texto_no_cnpj.set("CNPJ ")

        self.label_cnpj = tkinter.Label(self.frame_dados, font="Arial 10",
                                        bg="white", text="CNPJ:  ")

        self.entrada_do_cnpj = tkinter.Entry(self.frame_dados, font="Arial 8 bold",
                                             bg="white", fg="black", bd=2, width=30)
        self.entrada_do_cnpj.config(textvariable=texto_no_cnpj)

        self.label_cnpj.grid(row=2, column=1)
        self.entrada_do_cnpj.grid(row=2, column=2)

        # Telefone
        texto_no_telefone = tkinter.StringVar()
        texto_no_telefone.set("telefone")

        self.label_telefone = tkinter.Label(self.frame_dados, font="Arial 10",
                                            bg="white", text="Telefone:  ")

        self.entrada_do_telefone = tkinter.Entry(self.frame_dados, font="Arial 8 bold",
                                                 bg="white", fg="black", bd=2, width=30)
        self.entrada_do_telefone.config(textvariable=texto_no_telefone)

        self.label_telefone.grid(row=3, column=1)
        self.entrada_do_telefone.grid(row=3, column=2)

        self.window.mainloop()

    def criar_relatorio(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)
        self._apagar_relatorio()

        self._criar_loja()

        self.texto_relatorio.insert(1.0, self.loja)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def _criar_loja(self):
        nome = self.entrada_do_nome.get()
        cnpj = self.entrada_do_cnpj.get()
        telefone = self.entrada_do_telefone.get()

        loja = Loja(nome, cnpj, telefone)

        self.loja = loja

        salvar_loja_em_lista_do_main(nome, cnpj, telefone)

        #self._adicionar_em_lista_do_main(loja.nome, loja.cnpj, loja.telefone, None)

    def _adicionar_em_lista_do_main(self, primeira_variavel, segunda_variavel, terceira_variavel, quarta_variavel):
        super()._adicionar_em_lista_do_main(primeira_variavel, segunda_variavel, terceira_variavel, quarta_variavel)
        file = open("../entrada_de_dados/lista_de_lojas_criadas.py", "r")
        texto_lido = file.read()
        self.texto_temporario.insert(1.0, texto_lido)

        self.texto_temporario.insert("end", f'\n'
                                            f'nome = "{primeira_variavel}"\n'
                                            f'cnpj = "{self.segunda_variavel_sem_espaco}"\n'
                                            f'telefone = "{self.terceira_variavel_sem_espaco}"\n'
                                            f'loja_{self.primeira_variavel_sem_espaco} = Loja(nome, cnpj, telefone)\n'
                                            f'add_loja_na_lista_do_main(loja_{self.primeira_variavel_sem_espaco}, '
                                            f'variavel_contador_de_posicao_na_lista)\n'
                                            f'variavel_contador_de_posicao_na_lista += 1\n'
                                            f''
                                     )

        texto_reescrito = self.texto_temporario.get(1.0, "end")
        self.texto_temporario.delete(1.0, "end")
        file = open("../entrada_de_dados/lista_de_lojas_criadas.py", "w")
        file.write(texto_reescrito)
        file.close()


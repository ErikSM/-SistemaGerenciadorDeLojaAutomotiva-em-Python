import tkinter

from entrada_de_dados import validar_telefone, validar_email
from entrada_de_dados.editar_dicionario_cargos import criar_chave_da_loja_em_dicionario_cargos
from entrada_de_dados.editar_lista_lojas import salvar_loja_em_lista
from entrada_de_dados.gerador_de_codigo import criar_codigo_unico
from entrada_de_dados.lista_lojas import codigos_de_lojas_existentes
from entrada_de_dados.validar_documento import verificar_documento, Documento
from entrada_de_dados.validar_telefone import Telefone
from estrutura.AppBase import AppBase
from estrutura.Loja import Loja


class AppLoja(AppBase):

    def __init__(self, title):
        super().__init__(title)

        self.texto_temporario = tkinter.Text()
        self.loja = None
        self.mensagem_do_relatorio = None

        self.criacao_de_loja_autorizada = bool()

        self.frame_dados.pack(fill="both", side="top")
        self.botao_executar.grid(row=0, column=1)

        self.texto_relatorio.config(font=("Consolas", 9), width=60, height=20)
        self.texto_relatorio.pack(fill="both", side="bottom")

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

        # Email
        texto_no_email = tkinter.StringVar()
        texto_no_email.set("email")

        self.label_email = tkinter.Label(self.frame_dados, font="Arial 10", bg="white", text="Email:  ")

        self.entrada_do_email = tkinter.Entry(self.frame_dados, font="Arial 8 bold", bg="white", fg="black", bd=2,
                                              width=30)
        self.entrada_do_email.config(textvariable=texto_no_email)

        self.label_email.grid(row=4, column=1)
        self.entrada_do_email.grid(row=4, column=2)

    def criar_relatorio(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()

        self._criar_loja()

        self.texto_relatorio.insert(1.0, self.mensagem_do_relatorio)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def _criar_loja(self):
        nome = self.entrada_do_nome.get()
        cnpj = self.entrada_do_cnpj.get()
        telefone = self.entrada_do_telefone.get()
        email = self.entrada_do_email.get()
        codigo = criar_codigo_unico(codigos_de_lojas_existentes)

        if len(nome) == 0 or len(cnpj) == 0 or len(telefone) == 0 or len(email) == 0:
            self.criacao_de_loja_autorizada = False
            self.mensagem_do_relatorio = "Nao registrado\n\n  preencha todos os campos e tente novamente..."

        elif not Documento(cnpj).validar():
            self.criacao_de_loja_autorizada = False
            self.mensagem_do_relatorio = "\n ERrOr\n\n   CNPJ invalido"

        elif not Telefone(telefone).validar():
            self.criacao_de_loja_autorizada = False
            self.mensagem_do_relatorio = "\n ERrOr\n\n   TELEFONE invalido"

        elif validar_email.checar_email(email) == "erro_final" \
                or validar_email.checar_email(email) == "erro_formato" \
                or validar_email.checar_email(email) == "erro_operadora":
            self.criacao_de_loja_autorizada = False
            self.mensagem_do_relatorio = "\n ERrOr\n\n   EMAIL invalido"
        else:
            self.criacao_de_loja_autorizada = True
            self.mensagem_do_relatorio = str()

        if self.criacao_de_loja_autorizada:
            loja = Loja(nome, cnpj, telefone, email, codigo)
            salvar_loja_em_lista(loja)

            self.loja = loja

            self.mensagem_do_relatorio = self.loja
            criar_chave_da_loja_em_dicionario_cargos(self.loja)


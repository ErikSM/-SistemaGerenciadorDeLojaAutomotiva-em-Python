import tkinter

from entrada_de_dados import validar_email
from entrada_de_dados.dicionario_cargos import dicionario_de_cargos
from entrada_de_dados.editar_lista_funcionarios import salvar_funcionario_em_lista
from entrada_de_dados.gerador_de_codigo import criar_codigo_unico
from entrada_de_dados.lista_funcionarios import codigos_de_funcionarios_existentes
from entrada_de_dados.validar_documento import Documento
from entrada_de_dados.validar_telefone import Telefone
from estrutura import Loja
from estrutura.AppBase import AppBase
from estrutura.Funcionario import Funcionario


class AppFuncionario(AppBase):

    def __init__(self, title, loja: Loja):
        super().__init__(title)

        self.criacao_de_funcionario_autorizada = bool()

        self.loja = loja
        self.texto_temporario = tkinter.Text()
        self.cliente = None
        self.mensagem_do_relatorio = None

        self.lista_de_cargos_existentes = list()
        for i in dicionario_de_cargos:
            if dicionario_de_cargos[i]['cnpj'] == loja.cnpj:
                self.lista_de_cargos_existentes.append(f"{i}")

        self.frame_dados.pack(fill="both", side="top")
        self.botao_executar.grid(row=0, column=1)

        self.texto_relatorio.config(font=("Consolas", 9), width=60, height=20)
        self.texto_relatorio.pack(fill="both", side="bottom")

        # Funcionario
        texto_no_nome = tkinter.StringVar()
        texto_no_nome.set("funcionario")

        self.label_nome = tkinter.Label(self.frame_dados, font="Arial 10", bg="white", text="Funcionario:  ")

        self.entrada_nome = tkinter.Entry(self.frame_dados, font="Arial 8 bold", bg="white", fg="black", bd=2, width=30)
        self.entrada_nome.config(textvariable=texto_no_nome)

        self.label_nome.grid(row=1, column=1)
        self.entrada_nome.grid(row=1, column=2)

        # CPF
        texto_no_cpf = tkinter.StringVar()
        texto_no_cpf.set("CPF")

        self.label_cpf = tkinter.Label(self.frame_dados, font="Arial 10", bg="white", text="CPF:  ")

        self.entrada_do_cpf = tkinter.Entry(self.frame_dados, font="Arial 8 bold", bg="white", fg="black", bd=2,
                                            width=30)
        self.entrada_do_cpf.config(textvariable=texto_no_cpf)

        self.label_cpf.grid(row=2, column=1)
        self.entrada_do_cpf.grid(row=2, column=2)

        # Telefone
        texto_no_telefone = tkinter.StringVar()
        texto_no_telefone.set("telefone")

        self.label_telefone = tkinter.Label(self.frame_dados, font="Arial 10", bg="white", text="Telefone:  ")

        self.entrada_do_telefone = tkinter.Entry(self.frame_dados, font="Arial 8 bold", bg="white", fg="black", bd=2,
                                                 width=30)
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

        # Cargo
        self.label_cargo = tkinter.Label(self.frame_dados, font="Arial 10", bg="white", text="Cargo:  ")

        self.entrada_do_cargo = tkinter.Spinbox(self.frame_dados, values=self.lista_de_cargos_existentes)

        self.label_cargo.grid(row=5, column=1)
        self.entrada_do_cargo.grid(row=5, column=2)

    def criar_relatorio(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()

        self._criar_funcionario()

        self.texto_relatorio.insert(1.0, self.mensagem_do_relatorio)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def _criar_funcionario(self):
        nome = self.entrada_nome.get()
        cpf = self.entrada_do_cpf.get()
        telefone = self.entrada_do_telefone.get()
        email = self.entrada_do_email.get()
        codigo = criar_codigo_unico(codigos_de_funcionarios_existentes)
        cargo = dicionario_de_cargos[f"{self.entrada_do_cargo.get()}"]["cargo"]

        if len(nome) == 0 or len(cpf) == 0 or len(telefone) == 0 or len(email) == 0:
            self.criacao_de_funcionario_autorizada = False
            self.mensagem_do_relatorio = "Nao registrado\n\n  preencha todos os campos e tente novamente..."

        elif not Documento(cpf).validar():
            self.criacao_de_cliente_autorizada = False
            self.mensagem_do_relatorio = "\n ERrOr\n\n   CPF invalido"

        elif not Telefone(telefone).validar():
            self.criacao_de_cliente_autorizada = False
            self.mensagem_do_relatorio = "\n ERrOr\n\n   TELEFONE invalido"

        elif validar_email.checar_email(email) == "erro_final" \
                or validar_email.checar_email(email) == "erro_formato" \
                or validar_email.checar_email(email) == "erro_operadora":
            self.criacao_de_cliente_autorizada = False
            self.mensagem_do_relatorio = "\n ERrOr\n\n   EMAIL invalido"
        else:
            self.criacao_de_funcionario_autorizada = True
            self.mensagem_do_relatorio = str()

        if self.criacao_de_funcionario_autorizada:
            funcionario = Funcionario(nome, cpf, telefone, email, codigo)
            funcionario.cargo = cargo
            salvar_funcionario_em_lista(funcionario, self.loja)

            self.funcionario = funcionario
            self.funcionario.cnpj_loja = Documento(self.loja.cnpj)

            self.mensagem_do_relatorio = self.funcionario.mostrar_atributos_principais()

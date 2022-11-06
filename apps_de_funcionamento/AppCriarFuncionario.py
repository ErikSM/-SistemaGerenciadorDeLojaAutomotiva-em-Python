import tkinter

from entrada_de_dados.criar_e_adicionar_funcionarios_em_lista import salvar_funcionario_em_lista_do_main
from estrutura.AppBase import AppBase
from estrutura.Funcionario import Funcionario

''' 
Ainda em desenvolvimento

'''


class AppCriarFuncionario(AppBase):

    def __init__(self, title):
        super().__init__(title)

        self.texto_temporario = tkinter.Text()
        self.cliente = None
        self.mensagem_do_relatorio = None

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
        texto_no_cargo = tkinter.StringVar()
        texto_no_cargo.set("cargo")

        self.label_cargo = tkinter.Label(self.frame_dados, font="Arial 10", bg="white", text="Cargo:  ")

        self.entrada_do_cargo = tkinter.Entry(self.frame_dados, font="Arial 8 bold", bg="white", fg="black", bd=2,
                                              width=30)
        self.entrada_do_cargo.config(textvariable=texto_no_cargo)

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
        cargo = self.entrada_do_cargo.get()

        funcionario = Funcionario(nome, cpf, telefone, email, cargo)

        salvar_funcionario_em_lista_do_main(funcionario)

        self.funcionario = funcionario

        self.mensagem_do_relatorio = self.funcionario.mostrar_dados_do_funcionario()

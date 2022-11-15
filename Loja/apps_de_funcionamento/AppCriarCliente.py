import tkinter

from entrada_de_dados.editar_lista_clientes_registrados import salvar_cliente_em_lista_do_main
from estrutura.AppBase import AppBase
from estrutura.Cliente import Cliente


class AppCriarCliente(AppBase):

    def __init__(self, title):
        super().__init__(title)

        self.texto_temporario = tkinter.Text()
        self.cliente = None
        self.mensagem_do_relatorio = None

        # Cliente
        texto_no_nome = tkinter.StringVar()
        texto_no_nome.set("cliente")

        self.label_nome = tkinter.Label(self.frame_dados, font="Arial 10", bg="white", text="Cliente:  ")

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

    def criar_relatorio(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()

        self._criar_cliente()

        self.texto_relatorio.insert(1.0, self.mensagem_do_relatorio)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def _criar_cliente(self):
        nome = self.entrada_nome.get()
        cpf = self.entrada_do_cpf.get()
        telefone = self.entrada_do_telefone.get()
        email = self.entrada_do_email.get()

        cliente = Cliente(nome, cpf, telefone, email)

        salvar_cliente_em_lista_do_main(cliente)

        self.cliente = cliente

        self.mensagem_do_relatorio = self.cliente.mostrar_dados_do_cliente()

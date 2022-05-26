import tkinter
import datetime

from random import sample

from entrada_de_dados.criar_venda_em_arquivotxt_e_adicionar_em_lista import \
    criar_relatorio_de_venda_em_arquivo_de_texto, adicionar_relatorio_de_venda_em_lista_do_main, \
    remover_carro_vendido_da_lista_de_carros_registrados
from entrada_de_dados.lista_de_clientes_registrados import clientes_registrados
from entrada_de_dados.lista_de_vendas_efetuadas import vendas_registradas
from estrutura.AppBase import AppBase
from entrada_de_dados.lista_de_carros_registrados import carros_registrados
from estrutura.Loja import Loja
from estrutura.Venda import Venda
from estrutura.Carro import Carro
from apps_de_funcionamento.AppCriarLoja import AppCriarLoja
from apps_de_funcionamento.AppCarro import AppCarro
from apps_de_funcionamento.AppCliente import AppCliente


def abrir_registro_de_loja():
    return AppCriarLoja("Registro de Loja")


def abrir_registro_de_cliente():
    return AppCliente("Registro de Cliente")


def abrir_registro_de_carro():
    return AppCarro("Registro de Carro")


class AppLojaAberta(AppBase):

    def __init__(self, loja: Loja):
        super().__init__(loja)

        self.texto_temporario = tkinter.Text()

        self.lista_carros_da_loja = list()
        self.lista_clientes_da_loja = list()

        self.relatorio_de_venda_selecionado = None

        self.venda = None
        self.cliente_comprador = None
        self.carro_escolhido = None
        self.loja_de_transacao = loja

        self.window.resizable(2, 2)
        self.texto_relatorio.config(width=70, height=20)

        # \ Criando menu
        self.menu_principal = tkinter.Menu(self.window)

        # \\ Menu loja
        self.menu_loja = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_loja.add_command(label="Registrar Nova Loja", command=abrir_registro_de_loja)
        self.menu_principal.add_cascade(label="Loja", menu=self.menu_loja)
        self.window.config(menu=self.menu_principal)

        # \\ Menu cliente
        self.menu_cliente = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_cliente.add_command(label="Registrar Cliente", command=abrir_registro_de_cliente)

        self.menu_clientes_registrados = tkinter.Menu(self.menu_cliente, tearoff=0)
        for i in clientes_registrados:
            self.menu_clientes_registrados.add_command(label=f"Cliente:{i.nome}    cpf:{i.cpf}",
                                                       command=lambda cliente_select=i:
                                                       self.selecionar_cliente(cliente_select)
                                                       )
        self.menu_cliente.add_cascade(label="Clientes Registrados", menu=self.menu_clientes_registrados)

        self.menu_principal.add_cascade(label="Cliente", menu=self.menu_cliente)
        self.window.config(menu=self.menu_principal)

        # \\ Menu carro
        self.menu_carro = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_carro.add_command(label="Registrar Carro", command=abrir_registro_de_carro)

        self.menu_carros_registrados = tkinter.Menu(self.menu_carro, tearoff=0)
        for i in carros_registrados:
            self.menu_carros_registrados.add_command(label=f"Carro:{i.montadora}: {i.nome}    ${i.valor_avaliado}",
                                                     command=lambda carro_select=i:
                                                     self.selecionar_carro(carro_select)
                                                     )
        self.menu_carro.add_cascade(label="Carross Registrados", menu=self.menu_carros_registrados)

        self.menu_principal.add_cascade(label="Carro", menu=self.menu_carro)
        self.window.config(menu=self.menu_principal)

        # \\ Menu relatorios
        self.menu_relatorios = tkinter.Menu(self.menu_principal, tearoff=0)

        self.menu_relatorio_de_vendas = tkinter.Menu(self.menu_relatorios, tearoff=0)
        for i in vendas_registradas:
            self.menu_relatorio_de_vendas.add_command(label=f"(Venda)  codigo:{i.codigo}  data:{i.data}",
                                                      command=lambda venda_select=i:
                                                      self.exibir_relatorio_de_vendas_existente_na_lista(venda_select)
                                                      )
        self.menu_relatorios.add_cascade(label="Relatorio de Vendas", menu=self.menu_relatorio_de_vendas)
        self.window.config(menu=self.menu_relatorios)
        self.menu_principal.add_cascade(label="Relatorios", menu=self.menu_relatorios)
        self.window.config(menu=self.menu_principal)

        # Titulo da Loja Aberta
        self.label_title = tkinter.Label(self.frame_dados, text=f"Loja:({self.loja_de_transacao.nome})".title(),
                                         bg="white")
        self.label_title.config(font="Times 22 bold")
        self.label_title.grid(row=0, column=0, columnspan=2)

        # valor da venda
        self.label_da_lista_de_carros = tkinter.Label(self.frame_dados, text="  Digite o valor da negociacao  ->",
                                                      bg="white")
        self.label_da_lista_de_carros.grid(row=0, column=4)

        self.valor_de_venda_digitado = tkinter.Entry(self.frame_dados,  font="Verdanna 10 bold", width=30, bg="grey70",
                                                     fg="black", bd=4)
        self.valor_de_venda_digitado.insert("end", "0")
        self.valor_de_venda_digitado.grid(row=0, column=5)

        # carro selecionado
        self.label_da_lista_de_carros = tkinter.Label(self.frame_dados, font=('Verdanna', 10, 'italic', 'bold'),
                                                      text="Carro Selecionado:", bg="white")
        self.label_da_lista_de_carros.grid(row=1, column=0)

        self.opcoes_de_carros = tkinter.Entry(self.frame_dados, font=('Consolas', 10), width=110,
                                              disabledforeground="black")
        self.opcoes_de_carros.config(state=tkinter.DISABLED)
        self.opcoes_de_carros.grid(row=1, column=1, columnspan=5)

        # cliente selecionado
        self.label_da_lista_de_carros = tkinter.Label(self.frame_dados, font=('Verdanna', 10, 'italic', 'bold'),
                                                      text="Cliente Selecionado:", bg="white")
        self.label_da_lista_de_carros.grid(row=2, column=0)

        self.opcoes_de_clientes = tkinter.Entry(self.frame_dados, font=('Consolas', 10), width=110,
                                                disabledforeground="black")
        self.opcoes_de_clientes.config(state=tkinter.DISABLED)
        self.opcoes_de_clientes.grid(row=2, column=1, columnspan=5)

        # Botao Venda (reescrevendo AppBase)
        self.botao_adicionar.config(command=self.criar_relatorio, text="Efetivar Venda")
        self.botao_adicionar.grid(row=0, column=3)

    def criar_relatorio(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self._criar_venda()
        self.texto_relatorio.insert(1.0, self._escrever_relatorio_de_venda_criada())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def _criar_venda(self):
        self.valor_negociado = self.valor_de_venda_digitado.get()

        loja = self.loja_de_transacao
        cliente = self.cliente_comprador
        veiculo = self.carro_escolhido
        preco = self.valor_negociado
        data = datetime.date.today()
        codigo_de_venda = sample(range(0, 1000000), 1)
        codigo = codigo_de_venda[0]

        venda = Venda(data, codigo, loja, cliente, veiculo, preco)

        criar_relatorio_de_venda_em_arquivo_de_texto(venda, codigo)
        adicionar_relatorio_de_venda_em_lista_do_main(codigo)

        self.venda = venda

        self.valor_de_venda_digitado.delete(0, "end")

    def _escrever_relatorio_de_venda_criada(self):
        return f"codigo:{self.venda.codigo}   " \
               f"data:{self.venda.data}" \
               f"\n" \
               f"{self.venda.loja}" \
               f"{self.venda.cliente.mostrar_dados_do_cliente()}" \
               f"{self.venda.veiculo.mostrar_dados_do_veiculo()}" \
               f"\n" \
               f"Valor Negociado: ${self.venda.preco}"

    def exibir_relatorio_de_vendas_existente_na_lista(self, venda_select):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.relatorio_de_venda_selecionado = venda_select.mostrar_venda()
        self.texto_relatorio.insert(1.0, self.relatorio_de_venda_selecionado)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def selecionar_cliente(self, cliente_select):
        self.opcoes_de_clientes.config(state=tkinter.NORMAL)

        self.opcoes_de_clientes.delete(1, "end")
        self.opcoes_de_clientes.insert("end", cliente_select.mostrar_dados_do_cliente())
        self.cliente_comprador = cliente_select

        self.opcoes_de_clientes.config(state=tkinter.DISABLED)

    def selecionar_carro(self, carro_select):
        self.opcoes_de_carros.config(state=tkinter.NORMAL)

        self.opcoes_de_carros.delete(1, "end")
        self.opcoes_de_carros.insert("end", carro_select.mostrar_dados_do_veiculo())
        self.carro_escolhido = carro_select

        self.opcoes_de_carros.config(state=tkinter.DISABLED)
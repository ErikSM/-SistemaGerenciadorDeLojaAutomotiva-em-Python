import tkinter
import datetime

from random import sample

from entrada_de_dados.criar_venda_em_arquivotxt_e_adicionar_em_lista import \
    criar_relatorio_de_venda_em_arquivo_de_texto, adicionar_relatorio_de_venda_em_lista_do_main
from entrada_de_dados.lista_de_clientes_registrados import clientes_registrados
from entrada_de_dados.lista_de_vendas_efetuadas import vendas_registradas
from estrutura.AppBase import AppBase
from entrada_de_dados.lista_de_carros_registrados import carros_registrados
from estrutura.Loja import Loja
from estrutura.Venda import Venda
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

        self.relatorio_de_venda_selecionado = None
        self.texto_temporario = tkinter.Text()

        self.venda = None
        self.cliente_comprador = None
        self.carro_escolhido = None
        self.loja_de_transacao = loja

        # reescrevendo codigo(classe mae)
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
        self.menu_carro = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_carro.add_command(label="Registrar Cliente", command=abrir_registro_de_cliente)
        self.menu_principal.add_cascade(label="Cliente", menu=self.menu_carro)
        self.window.config(menu=self.menu_principal)

        # \\ Menu carro
        self.menu_carro = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_carro.add_command(label="Registrar Carro", command=abrir_registro_de_carro)
        self.menu_principal.add_cascade(label="Carro", menu=self.menu_carro)
        self.window.config(menu=self.menu_principal)

        # \\ Menu relatorios
        self.menu_relatorios = tkinter.Menu(self.menu_principal, tearoff=0)
        # \\\ Menu relatorios de vendas
        self.menu_relatorio_de_vendas = tkinter.Menu(self.menu_relatorios, tearoff=0)
        for i in vendas_registradas:
            self.menu_relatorio_de_vendas.add_command(label=f"(Venda)  codigo:{i.codigo}  data:{i.data}",
                                                      command=lambda
                                                          venda_select=i: self.exibir_relatorio_de_vendas_existente(
                                                          venda_select))
        self.menu_relatorios.add_cascade(label="Relatorio de Vendas", menu=self.menu_relatorio_de_vendas)
        self.window.config(menu=self.menu_relatorios)
        self.menu_principal.add_cascade(label="Relatorios", menu=self.menu_relatorios)
        self.window.config(menu=self.menu_principal)

        # Criando Titulo do nome da Loja Criada
        self.label_title = tkinter.Label(self.frame_dados, text=f"Loja:({self.loja_de_transacao.nome})".title(),
                                         bg="white")
        self.label_title.config(font="Times 22 bold")
        self.label_title.grid(row=0, column=0, columnspan=2)

        # label do valor da venda
        self.label_da_lista_de_carros = tkinter.Label(self.frame_dados, text="  Digite o valor da negociacao  ->",
                                                      bg="white")
        self.label_da_lista_de_carros.grid(row=0, column=4)

        # Entry do valor da venda
        self.valor_de_venda_digitado = tkinter.Entry(self.frame_dados, font="Verdanna 10 bold", width=30, bg="grey70",
                                                     fg="black", bd=4)
        self.valor_de_venda_digitado.insert("end", "0")
        self.valor_de_venda_digitado.grid(row=0, column=5)

        # label de carros
        self.label_da_lista_de_carros = tkinter.Label(self.frame_dados, text="Carros: ", bg="white")
        self.label_da_lista_de_carros.grid(row=1, column=0)

        # Spin de opcoes de carros
        self.lista_carros_da_loja = carros_registrados
        self.opcoes_de_carros = tkinter.Spinbox(self.frame_dados,
                                                values=self.lista_carros_da_loja, width=110)
        self.opcoes_de_carros.grid(row=1, column=1, columnspan=5)

        # label de clientes
        self.label_da_lista_de_carros = tkinter.Label(self.frame_dados, text="Clientes: ", bg="white")
        self.label_da_lista_de_carros.grid(row=2, column=0)

        # Spin de opcoes de clientes
        self.lista_clientes_da_loja = clientes_registrados
        self.opcoes_de_clientes = tkinter.Spinbox(self.frame_dados, values=self.lista_clientes_da_loja,
                                                  from_=0, to=len(clientes_registrados) - 1, width=110)
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

    def _escrever_relatorio_de_venda_criada(self):
        return f"codigo:{self.venda.codigo}   " \
               f"data:{self.venda.data}" \
               f"\n" \
               f"{self.venda.loja}" \
               f"{self.venda.cliente}" \
               f"{self.venda.veiculo}" \
               f"\n" \
               f"Valor Negociado: ${self.venda.preco}"

    def _criar_venda(self):
        self.carro_escolhido = self.opcoes_de_carros.get()
        self.cliente_comprador = self.opcoes_de_clientes.get()
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

    def retornar_appstart(self):
        self.window.quit()

    def exibir_relatorio_de_vendas_existente(self, venda_select):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()

        self.relatorio_de_venda_selecionado = venda_select.mostrar_venda()

        self.texto_relatorio.insert(1.0, self.relatorio_de_venda_selecionado)

        self.texto_relatorio.config(state=tkinter.DISABLED)

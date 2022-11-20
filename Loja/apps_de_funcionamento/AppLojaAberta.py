import tkinter

import datetime

from entrada_de_dados.gerador_de_codigo import criar_codigo_unico
from estrutura.AppBase import AppBase
from estrutura.Loja import Loja
from estrutura.Venda import Venda
from apps_de_funcionamento.AppCriarLoja import AppCriarLoja
from apps_de_funcionamento.AppCriarCarro import AppCriarCarro
from apps_de_funcionamento.AppCriarCliente import AppCriarCliente
from apps_de_funcionamento.AppCriarFuncionario import AppCriarFuncionario
from apps_de_funcionamento.AppSenhaEditar import AppSenhaEditar
from administracao.lucro_por_venda import criar_relatorio_de_lucro_sobre_a_venda_por_cada_veiculo
from administracao.total_de_lucro import criar_relatorio_de_lucro_total_de_vendas
from entrada_de_dados.lista_de_clientes_registrados import clientes_registrados
from entrada_de_dados.lista_de_funcionarios_registrados import funcionarios_registrados
from entrada_de_dados.lista_de_vendas_efetuadas import vendas_registradas, codigos_de_vendas_existentes
from entrada_de_dados.lista_de_carros_registrados import carros_registrados
from entrada_de_dados.editar_lista_lojas_criadas import remover_loja_da_lista_de_lojas_registrados
from entrada_de_dados.editar_lista_vendas_registradas import \
    adicionar_relatorio_de_venda_em_lista_do_main, \
    remover_carro_vendido_da_lista_de_carros_registrados


def abrir_registro_de_loja():
    return AppCriarLoja("Registro de Loja").window.mainloop()


def abrir_registro_de_cliente():
    return AppCriarCliente("Registro de Cliente").window.mainloop()


def abrir_registro_de_funcionario():
    return AppCriarFuncionario("Registro de Funcionario").window.mainloop()


def abrir_registro_de_carro():
    return AppCriarCarro("Registro de Carro").window.mainloop()


def abrir_alterador_de_senha(loja: Loja):
    AppSenhaEditar("Editar Senha", loja).window.mainloop()


class AppLojaAberta(AppBase):

    def __init__(self, loja: Loja):

        super().__init__(loja)
        self.texto_temporario = ""

        self.lista_carros_da_loja = list()
        self.lista_clientes_da_loja = list()

        self.relatorio_de_venda_selecionado = None

        self.venda = None
        self.funcionario_vendedor = None
        self.cliente_comprador = None
        self.carro_escolhido = None
        self.loja_de_transacao = loja

        self.window.geometry("+350+100")
        self.window.resizable(2, 2)
        self.frame_dados.pack(fill="y", side="top")
        self.texto_relatorio.config(width=70, height=20)

        self.texto_relatorio.config(state=tkinter.NORMAL)
        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, f"\n  (( Loja {loja.nome} ))\n\n\n"
                                         f"\n  OK!.."
                                         f"\n  Login na loja confirmado...")
        self.texto_relatorio.config(state=tkinter.DISABLED)

        # \ Criando menu
        self.menu_principal = tkinter.Menu(self.window)
        self.window.config(menu=self.menu_principal)

        # \\ Menu loja
        self.menu_loja = tkinter.Menu(self.menu_principal, tearoff=0)

        self.menu_loja.add_command(label=f"Sobre a Loja",
                                   command=lambda: self.mostrar_detalhes_da_loja(loja))

        self.menu_loja_editar = tkinter.Menu(self.menu_loja, tearoff=0)
        self.menu_loja_editar.add_command(label=f"Deletar Loja",
                                          command=lambda loja_select=loja: self.deletar_loja_aberta(loja_select))
        self.menu_loja_editar.add_command(label=f"Criar/Modificar Senha",
                                          command=lambda: abrir_alterador_de_senha(loja))
        self.menu_loja.add_cascade(label=f"Editar Loja (( {loja.nome} ))", menu=self.menu_loja_editar)

        self.menu_principal.add_cascade(label="Loja", menu=self.menu_loja)

        # \\ Menu funcionario
        self.menu_funcionario = tkinter.Menu(self.menu_principal, tearoff=0)

        self.menu_funcionario.add_command(label="Registrar Funcionario", command=abrir_registro_de_funcionario
                                          )

        self.menu_funcionarios_registrados = tkinter.Menu(self.menu_funcionario, tearoff=0)
        for i in funcionarios_registrados:
            self.menu_funcionarios_registrados.add_command(label=f"Funcionario:{i.nome} (({i.cargo['cargo']}))",
                                                           command=lambda funcionario_select=i:
                                                           self.selecionar_funcionario(funcionario_select)
                                                           )
        self.menu_funcionario.add_cascade(label="Funcionarios Registrados", menu=self.menu_funcionarios_registrados)

        self.menu_principal.add_cascade(label="Funcionario", menu=self.menu_funcionario)

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

        # \\ Menu carro
        self.menu_carro = tkinter.Menu(self.menu_principal, tearoff=0)

        self.menu_carro.add_command(label="Registrar Carro",
                                    command=abrir_registro_de_carro)

        self.menu_carros_registrados = tkinter.Menu(self.menu_carro, tearoff=0)
        for i in carros_registrados:
            self.menu_carros_registrados.add_command(label=f"Carro:{i.montadora}: {i.nome}    ${i.valor_de_aquisicao}",
                                                     command=lambda carro_select=i:
                                                     self.selecionar_carro(carro_select)
                                                     )
        self.menu_carro.add_cascade(label="Carros Registrados", menu=self.menu_carros_registrados)

        self.menu_principal.add_cascade(label="Carro", menu=self.menu_carro)

        # \\ Menu relatorios
        self.menu_relatorios = tkinter.Menu(self.menu_principal, tearoff=0)

        self.menu_relatorio_de_vendas = tkinter.Menu(self.menu_relatorios, tearoff=0)
        self.menu_detalhes_de_venda = tkinter.Menu(self.menu_relatorio_de_vendas, tearoff=0)
        for i in vendas_registradas:
            self.menu_detalhes_de_venda.add_command(label=f"(Venda)  codigo:{i.codigo}  data:{i.data}",
                                                    command=lambda venda_select=i:
                                                    self.exibir_relatorio_de_vendas_existente_na_lista(venda_select)
                                                    )
        self.menu_relatorio_de_vendas.add_cascade(label="Detalhes de cada Venda", menu=self.menu_detalhes_de_venda)
        self.menu_relatorio_de_vendas.add_command(label="Historico de vendas",
                                                  command=self.exibir_relatorio_de_historico_de_vendas)
        self.menu_relatorios.add_cascade(label="Relatorio de Vendas", menu=self.menu_relatorio_de_vendas)

        self.menu_relatorio_financeiro = tkinter.Menu(self.menu_relatorios, tearoff=0)
        self.menu_relatorio_financeiro.add_command(label="Lucro Total",
                                                   command=self.exibir_relatorio_do_total_de_lucro_das_vendas)
        self.menu_relatorio_financeiro.add_command(label="Historico de lucro",
                                                   command=self.exibir_relatorio_de_lucro_por_venda)
        self.menu_relatorios.add_cascade(label="Relatorio financeiro", menu=self.menu_relatorio_financeiro)

        self.menu_principal.add_cascade(label="Relatorios", menu=self.menu_relatorios)

        # Titulo da Loja Aberta
        self.label_title = tkinter.Label(self.frame_dados, text=f"Loja:({self.loja_de_transacao.nome})".title(),
                                         bg="white")
        self.label_title.config(font="Times 22 bold")
        self.label_title.grid(row=2, rowspan=2, column=0, columnspan=2)

        # Botao Venda (reescrevendo AppBase)
        self.botao_adicionar.config(command=self.criar_relatorio, text="Efetivar Venda")
        self.botao_adicionar.grid(row=2, column=3)

        # valor da venda
        self.label_valor_de_venda = tkinter.Label(self.frame_dados, text="  Digite o valor da negociacao  ->",
                                                  bg="white")
        self.label_valor_de_venda.grid(row=2, column=4)

        self.valor_de_venda_digitado = tkinter.Entry(self.frame_dados, font="Verdanna 10 bold", width=30, bg="grey70",
                                                     fg="black", bd=4)
        self.valor_de_venda_digitado.insert("end", "0")
        self.valor_de_venda_digitado.grid(row=2, column=5)

        # cliente selecionado
        self.label_cliente_pre_selecionado = tkinter.Label(self.frame_dados, font=('Verdanna', 10, 'italic', 'bold'),
                                                           text="Cliente Selecionado:", bg="white")
        self.label_cliente_pre_selecionado.grid(row=5, column=0)

        self.cliente_pre_selecionado = tkinter.Entry(self.frame_dados, font=('Consolas', 10), width=110,
                                                     disabledforeground="black")
        self.cliente_pre_selecionado.config(state=tkinter.DISABLED)
        self.cliente_pre_selecionado.grid(row=5, column=1, columnspan=5)

        # carro selecionado
        self.label_carro_pre_selecionado = tkinter.Label(self.frame_dados, font=('Verdanna', 10, 'italic', 'bold'),
                                                         text="Carro Selecionado:", bg="white")
        self.label_carro_pre_selecionado.grid(row=6, column=0)

        self.carro_pre_selecionado = tkinter.Entry(self.frame_dados, font=('Consolas', 10), width=110,
                                                   disabledforeground="black")
        self.carro_pre_selecionado.config(state=tkinter.DISABLED)
        self.carro_pre_selecionado.grid(row=6, column=1, columnspan=5)

        # vendedor selecionado
        self.label_funcionario_pre_selecionado = tkinter.Label(self.frame_dados,
                                                               font=('Verdanna', 10, 'italic', 'bold'),
                                                               text="Funcionario vendedor:   ", bg="white", fg="red")
        self.label_funcionario_pre_selecionado.grid(row=4, column=0)

        self.funcionario_pre_selecionado = tkinter.Entry(self.frame_dados, font=('Consolas', 10), width=110, bg="grey",
                                                         disabledbackground="grey")
        self.funcionario_pre_selecionado.config(state=tkinter.DISABLED)
        self.funcionario_pre_selecionado.grid(row=4, column=1, columnspan=5)

    def mostrar_detalhes_da_loja(self, loja: Loja):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, '\n(-Loja Registrada-)\n\n')
        self.texto_relatorio.insert("end", loja)

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def deletar_loja_aberta(self, loja: Loja):
        remover_loja_da_lista_de_lojas_registrados(loja.nome_da_variavel)
        return self.window.destroy()

    def selecionar_funcionario(self, funcionario_select):
        self.funcionario_pre_selecionado.config(state=tkinter.NORMAL)

        self.funcionario_pre_selecionado.delete(1, "end")
        self.funcionario_pre_selecionado.insert("end", funcionario_select.mostrar_atributos_principais())
        self.funcionario_vendedor = funcionario_select

        self.cliente_pre_selecionado.config(state=tkinter.DISABLED)

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, funcionario_select.mostrar_dados_do_funcionario())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def selecionar_cliente(self, cliente_select):
        self.cliente_pre_selecionado.config(state=tkinter.NORMAL)

        self.cliente_pre_selecionado.delete(1, "end")
        self.cliente_pre_selecionado.insert("end", cliente_select.mostrar_atributos_principais())
        self.cliente_comprador = cliente_select

        self.cliente_pre_selecionado.config(state=tkinter.DISABLED)

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, cliente_select.mostrar_dados_do_cliente())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def selecionar_carro(self, carro_select):
        self.carro_pre_selecionado.config(state=tkinter.NORMAL)

        self.carro_pre_selecionado.delete(1, "end")
        self.carro_pre_selecionado.insert("end", carro_select.mostrar_atributos_principais())
        self.carro_escolhido = carro_select

        self.carro_pre_selecionado.config(state=tkinter.DISABLED)

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, carro_select.mostrar_atributos_principais())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def criar_relatorio(self):
        if self.carro_escolhido is None or self.cliente_comprador is None:
            self.texto_relatorio.config(state=tkinter.NORMAL)

            self._apagar_relatorio()
            self.texto_relatorio.insert(7.0, "\n\n\n\n   "
                                             " $E##$&//$  !![ERRO] Selecione o veiculo e o cliente da venda no Menu !! "
                                             "   $E##$&//$ ---"
                                             "\n\n\n\n"
                                        )

            self.texto_relatorio.config(state=tkinter.DISABLED)
        else:
            self.texto_relatorio.config(state=tkinter.NORMAL)

            self._apagar_relatorio()
            self._criar_venda()
            self.texto_relatorio.insert(1.0, self._escrever_relatorio_de_venda_criada())

            self.texto_relatorio.config(state=tkinter.DISABLED)

            self.venda = None

    def _criar_venda(self):
        self.valor_negociado = self.valor_de_venda_digitado.get()

        loja = self.loja_de_transacao
        funcionario = self.funcionario_vendedor
        cliente = self.cliente_comprador
        veiculo = self.carro_escolhido
        preco = self.valor_negociado
        data = datetime.date.today()

        codigo = criar_codigo_unico(codigos_de_vendas_existentes)

        venda = Venda(data, codigo, loja, funcionario, cliente, veiculo, preco)

        adicionar_relatorio_de_venda_em_lista_do_main(venda)
        remover_carro_vendido_da_lista_de_carros_registrados(veiculo.nome_da_variavel, codigo)

        self.venda = venda

        self.funcionario_vendedor = None
        self.cliente_comprador = None
        self.carro_escolhido = None
        self.valor_de_venda_digitado.insert("end", "0")
        self.valor_de_venda_digitado.delete(0, "end")

    def _escrever_relatorio_de_venda_criada(self):
        return f"codigo:{self.venda.codigo}   " \
               f"data:{self.venda.data}" \
               f"\n" \
               f"{self.venda.loja}" \
               f"{self.venda.cliente.mostrar_atributos_principais()}" \
               f"{self.venda.veiculo.mostrar_atributos_principais()}" \
               f"\n" \
               f"Responsavel pela venda:{self.venda.funcionario.nome} cargo:{self.venda.funcionario.cargo['cargo']}\n" \
               f"\n" \
               f"Valor Negociado: ${self.venda.preco}"

    def exibir_relatorio_de_vendas_existente_na_lista(self, venda_select):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.relatorio_de_venda_selecionado = venda_select.mostrar_dados_da_venda()
        self.texto_relatorio.insert(1.0, self.relatorio_de_venda_selecionado)

        self.texto_relatorio.config(state=tkinter.DISABLED)

        self.relatorio_de_venda_selecionado = None

    def exibir_relatorio_do_total_de_lucro_das_vendas(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, criar_relatorio_de_lucro_total_de_vendas())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def exibir_relatorio_de_lucro_por_venda(self):

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, criar_relatorio_de_lucro_sobre_a_venda_por_cada_veiculo())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def exibir_relatorio_de_historico_de_vendas(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, "\n       ((Historico de Vendas))\n\n\n")

        for i in vendas_registradas:
            self.texto_relatorio.insert("end", f""
                                               f"   >>  codigo:{i.codigo}  << \n"
                                               f"\n"
                                               f"data:{i.data}  "
                                               f"Loja:{i.loja.nome}  "
                                               f"Cliente:{i.cliente.nome}  "
                                               f"**Valor Negociado:{i.preco}**\n"
                                               f"{'-' * 98}"
                                        )

        self.texto_relatorio.config(state=tkinter.DISABLED)

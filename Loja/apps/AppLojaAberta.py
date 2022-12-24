import tkinter

import datetime

from administracao.desempenho_funcionarios import criar_relatorio_de_comissoes_pagas_por_cada_funcionario
from administracao.ranking import organizar_rankings_da_loja
from entrada_de_dados.gerador_de_codigo import criar_codigo_unico
from entrada_de_dados.editar_lista_lojas import remover_loja_da_lista
from entrada_de_dados.editar_lista_vendas import adicionar_venda_em_lista, remover_carro_vendido_da_lista_carros
from entrada_de_dados.lista_carros import carros_registrados
from entrada_de_dados.lista_clientes import clientes_registrados
from entrada_de_dados.lista_funcionarios import funcionarios_registrados
from entrada_de_dados.lista_vendas import codigos_de_vendas_existentes, vendas_registradas
from entrada_de_dados.mascarar_preco import mascarar_preco
from estrutura import Loja
from estrutura.AppBase import AppBase
from apps.AppCriarLoja import AppCriarLoja
from apps.AppCriarCarro import AppCriarCarro
from apps.AppCriarCliente import AppCriarCliente
from apps.AppCriarFuncionario import AppCriarFuncionario
from apps.AppSenhaEditar import AppSenhaEditar
from administracao.lucro_por_venda import criar_relatorio_de_lucro_sobre_a_venda_por_cada_veiculo
from administracao.total_de_lucro import criar_relatorio_de_lucro_total_de_vendas
from estrutura.Venda import Venda


def abrir_registro_de_loja():
    return AppCriarLoja("Registro de Loja").window.mainloop()


def abrir_registro_de_cliente(loja: Loja):
    return AppCriarCliente("Registro de Cliente", loja).window.mainloop()


def abrir_registro_de_funcionario(loja: Loja):
    return AppCriarFuncionario("Registro de Funcionario", loja).window.mainloop()


def abrir_registro_de_carro(loja: Loja):
    return AppCriarCarro("Registro de Carro", loja).window.mainloop()


def abrir_alterador_de_senha(loja: Loja):
    AppSenhaEditar("Editar Senha", loja).window.mainloop()


class AppLojaAberta(AppBase):

    def __init__(self, loja: Loja):

        super().__init__(loja)

        for carro in carros_registrados:
            if carro.cnpj_loja == int(loja.cnpj):
                loja.adicionar_carro(carro)
        for cliente in clientes_registrados:
            if cliente.cnpj_loja == int(loja.cnpj):
                loja.adicionar_cliente(cliente)
        for funcionario in funcionarios_registrados:
            if funcionario.cnpj_loja == int(loja.cnpj):
                loja.adicionar_funcionario(funcionario)
        for venda in vendas_registradas:
            if int(venda.loja.cnpj) == int(loja.cnpj):
                loja.adicionar_venda(venda)

        self.loja_de_transacao = loja
        self.dicionario_da_loja = self.loja_de_transacao.dicionario_da_loja

        self.venda = None
        self.funcionario_vendedor = None
        self.cliente_comprador = None
        self.carro_escolhido = None

        self.validar = None

        self.relatorio_de_venda_selecionado = None

        self.texto_temporario = None

        self.window.title(loja.mostrar_dados())
        self.window.geometry("+350+100")
        self.window.resizable(False, False)
        self.frame_dados.pack(fill="y", side="top")
        self.texto_relatorio.config(width=70, height=20, font=("Consolas", 10))

        self.retornar_data_e_hora()

        self.texto_relatorio.config(state=tkinter.NORMAL)
        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, f"\n  (( Loja {loja.nome} ))\n\n\n"
                                         f"\n  OK!.."
                                         f"\n  Login na loja confirmado...")
        self.texto_relatorio.config(state=tkinter.DISABLED)

        # \\\ MENU
        self.menu_principal = tkinter.Menu(self.window)
        self.window.config(menu=self.menu_principal)

        # \\ Menu loja
        self.menu_loja = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Loja", menu=self.menu_loja)
        # \ informacoes
        self.menu_loja.add_command(label=f"Sobre a Loja",
                                   command=lambda: self.mostrar_detalhes_da_loja(self.loja_de_transacao))
        # \ editar
        self.menu_loja_editar = tkinter.Menu(self.menu_loja, tearoff=0)
        self.menu_loja_editar.add_command(label=f"Deletar Loja",
                                          command=lambda loja_select=loja: self.deletar_loja_aberta(loja_select))
        self.menu_loja_editar.add_command(label=f"Criar/Modificar Senha",
                                          command=lambda: abrir_alterador_de_senha(loja))
        self.menu_loja.add_cascade(label=f"Editar Loja (( {loja.nome} ))", menu=self.menu_loja_editar)

        # \\ Menu funcionario
        self.menu_funcionario = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Funcionario", menu=self.menu_funcionario)
        # \ registrar
        self.menu_funcionario.add_command(label="Registrar Funcionario",
                                          command=lambda: abrir_registro_de_funcionario(self.loja_de_transacao))
        # \ selecionar
        self.menu_funcionarios_registrados = tkinter.Menu(self.menu_funcionario, tearoff=0)
        for i in self.dicionario_da_loja["funcionarios"]:
            self.menu_funcionarios_registrados.add_command(label=f"Funcionario:{i.nome} (({i.cargo['cargo']}))",
                                                           command=lambda funcionario_select=i:
                                                           self.selecionar_funcionario(funcionario_select))
        self.menu_funcionario.add_cascade(label="Funcionarios Registrados", menu=self.menu_funcionarios_registrados)

        # \\ Menu cliente
        self.menu_cliente = tkinter.Menu(self.menu_principal, tearoff=0)
        # \ registrar
        self.menu_cliente.add_command(label="Registrar Cliente",
                                      command=lambda: abrir_registro_de_cliente(self.loja_de_transacao))
        # \ selecionar
        self.menu_clientes_registrados = tkinter.Menu(self.menu_cliente, tearoff=0)
        for i in self.dicionario_da_loja["clientes"]:
            self.menu_clientes_registrados.add_command(label=f"Cliente:{i.nome}  Cpf:{i.cpf}",
                                                       command=lambda cliente_select=i:
                                                       self.selecionar_cliente(cliente_select))
        self.menu_cliente.add_cascade(label="Clientes Registrados", menu=self.menu_clientes_registrados)
        self.menu_principal.add_cascade(label="Cliente", menu=self.menu_cliente)

        # \\ Menu carro
        self.menu_carro = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Carro", menu=self.menu_carro)
        # \ registrar
        self.menu_carro.add_command(label="Registrar Carro",
                                    command=lambda: abrir_registro_de_carro(self.loja_de_transacao))
        # \ selecionar
        self.menu_carros_registrados = tkinter.Menu(self.menu_carro, tearoff=0)
        for i in self.dicionario_da_loja["carros"]:
            self.menu_carros_registrados.add_command(label=f"Carro:{i.montadora}: {i.nome}    ${i.valor_de_aquisicao}",
                                                     command=lambda carro_select=i:
                                                     self.selecionar_carro(carro_select))
        self.menu_carro.add_cascade(label="Carros Registrados", menu=self.menu_carros_registrados)

        # \\ Menu relatorios
        self.menu_relatorios = tkinter.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label="Relatorios", menu=self.menu_relatorios)
        # \ vendas
        self.menu_relatorio_de_vendas = tkinter.Menu(self.menu_relatorios, tearoff=0)
        self.menu_detalhes_de_venda = tkinter.Menu(self.menu_relatorio_de_vendas, tearoff=0)
        for i in self.dicionario_da_loja["vendas"]:
            self.menu_detalhes_de_venda.add_command(label=f"(Venda)  codigo:{i.codigo}  data:{i.data}",
                                                    command=lambda venda_select=i:
                                                    self.exibir_relatorio_de_vendas_existente_na_lista(venda_select))
        self.menu_relatorio_de_vendas.add_cascade(label="Detalhes de cada Venda", menu=self.menu_detalhes_de_venda)
        self.menu_relatorio_de_vendas.add_command(label="Historico de vendas",
                                                  command=self.exibir_relatorio_de_historico_de_vendas)
        self.menu_relatorios.add_cascade(label="Relatorio de Vendas", menu=self.menu_relatorio_de_vendas)
        #  \ financeiro
        self.menu_relatorio_financeiro = tkinter.Menu(self.menu_relatorios, tearoff=0)
        self.menu_relatorio_financeiro.add_command(label="Lucro Total",
                                                   command=self.exibir_relatorio_do_total_de_lucro_das_vendas)
        self.menu_relatorio_financeiro.add_command(label="Historico de lucro",
                                                   command=self.exibir_relatorio_de_lucro_por_venda)
        self.menu_relatorios.add_cascade(label="Relatorio financeiro", menu=self.menu_relatorio_financeiro)
        # \ comissoes
        self.menu_relatorio_comissao = tkinter.Menu(self.menu_relatorios, tearoff=0)
        self.menu_relatorio_comissao.add_command(label="Comissoes pagas",
                                                 command=self.exibir_relatorio_de_comissoes)
        self.menu_relatorios.add_cascade(label="Relatorio de desempenho", menu=self.menu_relatorio_comissao)

        # \ ranking
        self.menu_relatorio_ranking = tkinter.Menu(self.menu_relatorios, tearoff=0)
        self.menu_relatorio_ranking.add_command(label="Carros mais vendidos",
                                                command=self.exibir_relatorio_de_ranking_de_carros)
        self.menu_relatorio_ranking.add_command(label="Melhores clientes",
                                                command=self.exibir_relatorio_de_ranking_de_clientes)
        self.menu_relatorios.add_cascade(label="Ranking", menu=self.menu_relatorio_ranking)

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
                                                               text="Funcionario vendedor:   ", bg="grey90", fg="red")
        self.label_funcionario_pre_selecionado.grid(row=4, column=0)

        self.funcionario_pre_selecionado = tkinter.Entry(self.frame_dados, font=('Consolas', 10), width=110, bg="grey",
                                                         disabledbackground="grey")
        self.funcionario_pre_selecionado.config(state=tkinter.DISABLED)
        self.funcionario_pre_selecionado.grid(row=4, column=1, columnspan=5)

    def mostrar_detalhes_da_loja(self, loja: Loja):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, '\n(-Loja Registrada-)\n')
        self.texto_relatorio.insert("end", loja.mostrar_dados())

        for tipo in self.dicionario_da_loja:
            self.texto_relatorio.insert("end", f'\n\n\n\n(({tipo}))\n')
            self.texto_relatorio.insert("end", f'{"--" * 30}')

            lista = self.dicionario_da_loja[tipo]
            for conteudo in lista:
                self.texto_relatorio.insert("end", conteudo.mostrar_dados())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def deletar_loja_aberta(self, loja: Loja):
        remover_loja_da_lista(loja.nome_da_variavel)
        return self.window.destroy()

    def selecionar_funcionario(self, funcionario_select):
        self.funcionario_pre_selecionado.config(state=tkinter.NORMAL)

        self.funcionario_pre_selecionado.delete(1, "end")
        self.funcionario_pre_selecionado.insert("end", funcionario_select.mostrar_atributos_principais())
        self.funcionario_vendedor = funcionario_select

        self.cliente_pre_selecionado.config(state=tkinter.DISABLED)

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, funcionario_select.mostrar_dados())

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def selecionar_cliente(self, cliente_select):
        self.cliente_pre_selecionado.config(state=tkinter.NORMAL)

        self.cliente_pre_selecionado.delete(1, "end")
        self.cliente_pre_selecionado.insert("end", cliente_select.mostrar_atributos_principais())
        self.cliente_comprador = cliente_select

        self.cliente_pre_selecionado.config(state=tkinter.DISABLED)

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, cliente_select.mostrar_dados())

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
            self.texto_relatorio.insert(7.0, ""
                                             "\n\n\n\n   "
                                             " $E##$&//$  !![ERRO] Selecione o veiculo e o cliente da venda no Menu !! "
                                             "   $E##$&//$ ---"
                                             "\n\n\n\n")

            self.texto_relatorio.config(state=tkinter.DISABLED)
        else:
            self.texto_relatorio.config(state=tkinter.NORMAL)

            self._apagar_relatorio()
            self._criar_venda()
            if self.validar:
                self.texto_relatorio.insert(1.0, self._escrever_relatorio_de_venda_criada())
            else:
                self.texto_relatorio.insert(1.0, "ErRor\n valor digitado invalido!")

            self.texto_relatorio.config(state=tkinter.DISABLED)

            self.venda = None
            self.validar = None

    def _criar_venda(self):
        try:
            float(self.valor_de_venda_digitado.get())
            self.validar = True
        except ValueError:
            self.validar = False

        if self.validar:
            self.valor_negociado = self.valor_de_venda_digitado.get()

            loja = self.loja_de_transacao
            funcionario = self.funcionario_vendedor
            cliente = self.cliente_comprador
            veiculo = self.carro_escolhido
            preco = self.valor_negociado
            data = datetime.date.today()
            codigo = criar_codigo_unico(codigos_de_vendas_existentes)

            venda = Venda(data, codigo, loja, funcionario, cliente, veiculo, preco)
            adicionar_venda_em_lista(venda)
            remover_carro_vendido_da_lista_carros(veiculo.nome_da_variavel, codigo)
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
               f"Valor Negociado: {mascarar_preco(self.venda.preco)}"

    def exibir_relatorio_de_vendas_existente_na_lista(self, venda_select):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.relatorio_de_venda_selecionado = venda_select.mostrar_dados()
        self.texto_relatorio.insert(1.0, self.relatorio_de_venda_selecionado)

        self.texto_relatorio.config(state=tkinter.DISABLED)

        self.relatorio_de_venda_selecionado = None

    def exibir_relatorio_do_total_de_lucro_das_vendas(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0,
                                    criar_relatorio_de_lucro_total_de_vendas(self.loja_de_transacao))

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def exibir_relatorio_de_lucro_por_venda(self):

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0,
                                    criar_relatorio_de_lucro_sobre_a_venda_por_cada_veiculo(self.loja_de_transacao))

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def exibir_relatorio_de_historico_de_vendas(self):
        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0, "\n       ((Historico de Vendas))\n\n\n")
        for i in self.dicionario_da_loja["vendas"]:
            self.texto_relatorio.insert("end", f""
                                               f"(codigo:{i.codigo}): "
                                               f"data:{i.data}  "
                                               f"Loja:{i.loja.nome}  "
                                               f"Cliente:{i.cliente.nome}  "
                                               f"**Valor Negociado:{i.preco}**\n"
                                        # f"{'-' * 98}\n"
                                        )

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def exibir_relatorio_de_comissoes(self):

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_relatorio.insert(1.0,
                                    criar_relatorio_de_comissoes_pagas_por_cada_funcionario(self.loja_de_transacao))

        self.texto_relatorio.config(state=tkinter.DISABLED)

    def exibir_relatorio_de_ranking_de_carros(self):

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_temporario = organizar_rankings_da_loja(self.loja_de_transacao, "carros")
        self.texto_relatorio.insert(1.0, self.texto_temporario)

        self.texto_relatorio.config(state=tkinter.DISABLED)

        self.texto_temporario = None

    def exibir_relatorio_de_ranking_de_clientes(self):

        self.texto_relatorio.config(state=tkinter.NORMAL)

        self._apagar_relatorio()
        self.texto_temporario = organizar_rankings_da_loja(self.loja_de_transacao, "clientes")
        self.texto_relatorio.insert(1.0, self.texto_temporario)

        self.texto_relatorio.config(state=tkinter.DISABLED)

        self.texto_temporario = None

from ferramentas.Preco import Preco
from ferramentas.Documento import Documento
from ferramentas.Telefone import Telefone
from estrutura.Funcionario import Funcionario
from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Veiculo import Veiculo


class Venda:

    def __init__(self,
                 loja: Loja,
                 funcionario: Funcionario,
                 cliente: Cliente,
                 veiculo: Veiculo,
                 informacoes: tuple):

        self.data = informacoes[0]
        self.codigo = informacoes[1]
        self.__preco = informacoes[2]

        self.__loja = loja
        self.__funcionario = funcionario
        self.__cliente = cliente
        self.__veiculo = veiculo

        self.__comissao_sobre_a_venda = self.calcular_comissao_sobre_a_venda()
        self.__lucro_sobre_a_venda = self.calcular_lucro_sobre_a_venda()

        self.nome_da_variavel = ""

    def __str__(self):
        return f'# ((Dados da Venda)):\n\n' \
               f'data = "{self.data}"\n\n' \
               f'codigo = "{self.codigo}"\n\n' \
               f'# (loja)\n' \
               f'from entrada_de_dados.lista_lojas import {self.__loja.nome_da_variavel}\n' \
               f'loja = {self.__loja.nome_da_variavel}\n\n' \
               f'# (funcionario)\n' \
               f'from entrada_de_dados.lista_funcionarios import {self.__funcionario.nome_da_variavel}\n' \
               f'funcionario = {self.__funcionario.nome_da_variavel}\n\n' \
               f'# (cliente)\n' \
               f'from entrada_de_dados.lista_clientes import {self.__cliente.nome_da_variavel}\n' \
               f'cliente = {self.__cliente.nome_da_variavel}\n\n' \
               f'# (veiculo)\n' \
               f'from entrada_de_dados.lista_carros import {self.__veiculo.nome_da_variavel}\n' \
               f'carro = {self.__veiculo.nome_da_variavel}\n' \
               f'\n' \
               f'valor_negociado = "{self.__preco}"\n' \
               f'\n' \
               f'info_de_registro = (data, codigo, valor_negociado)\n' \
               f'venda_{self.codigo} = Venda(loja, funcionario, cliente, carro, info_de_registro)\n' \
               f'\n'

    def mostrar_dados(self):
        return f'\ncodigo:{self.codigo}   data:{self.data}  \n' \
               f'\n' \
               f'((Dados da Venda)):\n' \
               f'Loja:{self.__loja.nome}     cnpj:{Documento(self.__loja.cnpj)}  \n' \
               f'Funcionario:{self.__funcionario.nome}     cargo:{self.__funcionario.cargo["cargo"]}  \n' \
               f'Cliente:{self.__cliente.nome}     contato:{Telefone(self.__cliente.telefone)}   \n\n' \
               f'((Veiculo)):{self.__veiculo.mostrar_dados()}\n' \
               f'\n' \
               f'((Valor Negociado)):\n' \
               f'Preco: "{Preco(self.__preco)}"\n' \
               f'\n' \
               f'Comissao sobre a venda = {Preco(self.__comissao_sobre_a_venda)}\n' \
               f'\n'

    def relatorio_de_venda(self):
        return f'codigo:{self.codigo}   ' \
               f'data:{self.data}   ' \
               f'\n' \
               f'{self.__loja}' \
               f'{self.__cliente.mostrar_atributos_principais()}' \
               f'{self.__veiculo.mostrar_atributos_principais()}' \
               f'\n' \
               f'Responsavel pela venda:{self.__funcionario.nome} cargo:{self.__funcionario.cargo["cargo"]}\n' \
               f'\n' \
               f'Valor Negociado: {Preco(self.__preco)}'

    def relatorio_resumido(self):
        return f'(codigo:{self.codigo}): ' \
               f'data:{self.data}  ' \
               f'Loja:{self.__loja.nome}  ' \
               f'Cliente:{self.__cliente.nome}  ' \
               f'**Valor Negociado:{self.__preco}**\n'

    def calcular_comissao_sobre_a_venda(self):
        valor_calculado = float("".join(self.__preco.split())) * float(self.__funcionario.comissao)
        return valor_calculado

    def calcular_lucro_sobre_a_venda(self):
        valor_gasto = float("".join(self.__veiculo.valor_de_aquisicao.split()))
        valor_ganho = float("".join(self.__preco.split()))
        lucro = float((valor_ganho - self.__comissao_sobre_a_venda) - valor_gasto)
        return lucro

    @property
    def loja(self):
        return self.__loja

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def cliente(self):
        return self.__cliente

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def comissao_sobre_a_venda(self):
        return self.__comissao_sobre_a_venda

    @property
    def lucro_sobre_a_venda(self):
        return self.__lucro_sobre_a_venda

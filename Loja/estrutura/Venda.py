from estrutura.Cliente import Cliente
from estrutura.Loja import Loja
from estrutura.Veiculo import Veiculo


class Venda:

    def __init__(self, data, codigo, loja: Loja, cliente: Cliente, veiculo: Veiculo, preco):
        self.data = data
        self.codigo = codigo

        self.__loja = loja
        self.__cliente = cliente
        self.__veiculo = veiculo

        self.__preco = preco

    def __str__(self):
        return f'# codigo:{self.codigo}   data:{self.data}\n' \
               f'\n' \
               f'from estrutura.Cliente import Cliente\n' \
               f'from estrutura.Loja import Loja\n' \
               f'from estrutura.Carro import Carro\n' \
               f'from estrutura.Venda import Venda\n' \
               f'\n\n' \
               f'# ((Dados da Venda)):\n\n' \
               f'data = "{self.data}"\n\n' \
               f'codigo = "{self.codigo}"\n\n' \
               f'# (loja)' \
               f'{self.__loja}\n' \
               f'loja = Loja(loja, cnpj, contato)\n\n' \
               f'# (cliente)' \
               f'{self.__cliente.mostrar_dados_do_cliente()}\n' \
               f'cliente = Cliente(nome, cpf, telefone, email)\n\n' \
               f'# (veiculo)' \
               f'{self.__veiculo.mostrar_dados_do_veiculo()}\n' \
               f'carro = Carro(montadora, nome, ano, valor_avaliado)\n' \
               f'\n' \
               f'valor_negociado = "{self.__preco}"\n' \
               f'\n' \
               f'venda_{self.codigo} = Venda(data, codigo, loja, cliente, carro, valor_negociado)\n' \
               f'\n'

    def mostrar_venda(self):
        return f'codigo:{self.codigo}   data:{self.data}  \n' \
               f'\n' \
               f'((Dados da Venda)):\n' \
               f'Loja:{self.__loja.nome}     cnpj:{self.__loja.cnpj}  \n' \
               f'Cliente:{self.__cliente.nome}     contato:{self.__cliente.telefone}   \n\n' \
               f'((Veiculo)):{self.__veiculo.mostrar_dados_do_veiculo()}\n' \
               f'\n' \
               f'((Valor Negociado)):\n' \
               f'PrecoY$: "{self.__preco}"\n' \
               f'\n '

    @property
    def loja(self):
        return self.__loja

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

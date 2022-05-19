from estrutura.Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, montadora, nome, ano, valor_avaliado):
        super().__init__(montadora, nome, ano, valor_avaliado)

    def abstractmethod(self):
        pass


class Loja:

    def __init__(self, nome, cnpj, telefone):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__telefone = telefone
        self.__senha = None
        self.posicao_na_lista = None
        self.nome_da_variavel = " "
        self.lista_de_carros_vinculados_a_loja = list()

    def __str__(self):
        return f'\nloja = "{self.__nome}"   \n' \
               f'cnpj = "{self.__cnpj}"   \n' \
               f'contato = "{self.__telefone}"   \n'

    def mostrar_sem_pular_linha(self):
        return f'loja:{self.__nome}   ' \
                f'cnpj:{self.__cnpj}   ' \
                f'contato:{self.__telefone}   '

    @property
    def nome(self):
        return self.__nome

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

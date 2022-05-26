class Loja:

    def __init__(self, nome, cnpj, telefone):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__telefone = telefone
        self.posicao_na_lista = None

    def __str__(self):
        return f'\nloja = "{self.__nome}   "\n' \
               f'cnpj = "{self.__cnpj}"   \n' \
               f'contato = "{self.__telefone}   "\n'

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

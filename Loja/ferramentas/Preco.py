class Preco:

    def __init__(self, valor):

        self.valor = f'{float(valor):.2f}'
        self.preco = self.mascarar_preco()

    def __str__(self):
        return self.preco

    def mascarar_preco(self):
        referencia = self._encontrar_posicao_do_caractere()
        parte_um = self.valor[:referencia]
        parte_dois = self.valor[referencia + 1:]

        return 'R$:{},{}'.format(parte_um, parte_dois)

    def _encontrar_posicao_do_caractere(self):
        indice = 0
        while indice < len(self.valor):
            if self.valor[indice] == ".":
                return indice
            indice = indice + 1

        return -1

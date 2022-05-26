import tkinter
from random import sample

from entrada_de_dados.salvar_dados_adicionados_no_programa import atualizar_informacoes
from estrutura.Carro import Carro


def _escrever_objeto_carro(carro: Carro):
    codigo_do_veiculo = sample(range(0, 1000000), 1)
    codigo = codigo_do_veiculo[0]

    montadora_espalhado = carro.montadora.split()
    montadora_sem_espaco = "_".join(montadora_espalhado)
    montadora_da_variavel_do_carro = montadora_sem_espaco.lower()

    nome_espalhado = carro.nome.split()
    nome_sem_espaco = "_".join(nome_espalhado)
    nome_da_variavel_do_carro = nome_sem_espaco.lower()
    return f"\n" \
           f'montadora = "{carro.montadora}"\n' \
           f'nome = "{carro.nome}"\n' \
           f'ano = "{carro.ano}"\n' \
           f'preco = "{carro.preco}"' \
           f'\n' \
           f'carro_{montadora_da_variavel_do_carro}_' \
           f'{nome_da_variavel_do_carro}_{codigo} = Carro(montadora, nome, ano, preco)' \
           f'\n' \
           f'add_carro_na_lista_do_main(carro_{montadora_da_variavel_do_carro}_' \
           f'{nome_da_variavel_do_carro}_{codigo}, "carro_{montadora_da_variavel_do_carro}_' \
           f'{nome_da_variavel_do_carro}_{codigo}")' \
           f'\n' \
           f'_atualizar_contador_da_lista()' \
           f'\n'


def salvar_carro_em_lista_do_main(carro: Carro):
    texto_temporario = tkinter.Text()

    arquivo = open("../entrada_de_dados/lista_de_carros_registrados.py", "r")
    arquivo_lido = arquivo.read()
    texto_temporario.insert(1.0, arquivo_lido)

    arquivo_escrito = _escrever_objeto_carro(carro)

    file = open("../entrada_de_dados/lista_de_carros_registrados.py", "w")
    texto_temporario.insert("end", arquivo_escrito)
    file.write(texto_temporario.get(1.0, "end"))

    atualizar_informacoes(arquivo, file)

    texto_temporario.delete(1.0, "end")
    arquivo.close()
    file.close()

from entrada_de_dados.salvar_modificacoes_no_arquivo import abrir_modificar_e_salvar_arquivo
from estrutura.Carro import Carro


def salvar_carro_em_lista_do_main(carro: Carro):
    endereco_do_arquivo = "entrada_de_dados/lista_de_carros_registrados"

    escrever = _escrever_objeto_carro(carro)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_objeto_carro(carro: Carro):
    variavel_da_montadora_do_carro = _montadora_sem_espaco(carro)
    nome_da_variavel_do_carro = _nome_sem_espaco(carro)
    return f"\n" \
           f'{carro.mostrar_atributos_principais()}' \
           f'carro_{variavel_da_montadora_do_carro}_' \
           f'{nome_da_variavel_do_carro}_{carro.codigo} = Carro(montadora, nome, ano, preco, codigo)' \
           f'\n' \
           f'add_carro_na_lista_do_main(carro_{variavel_da_montadora_do_carro}_' \
           f'{nome_da_variavel_do_carro}_{carro.codigo}, "carro_{variavel_da_montadora_do_carro}_' \
           f'{nome_da_variavel_do_carro}_{carro.codigo}")' \
           f'\n'


def _montadora_sem_espaco(carro: Carro):
    montadora_espalhado = carro.montadora.split()
    montadora_sem_espaco = "_".join(montadora_espalhado)
    variavel_da_montadora_do_carro = montadora_sem_espaco.lower()
    return variavel_da_montadora_do_carro


def _nome_sem_espaco(carro: Carro):
    nome_espalhado = carro.nome.split()
    nome_sem_espaco = "_".join(nome_espalhado)
    nome_da_variavel_do_carro = nome_sem_espaco.lower()
    return nome_da_variavel_do_carro


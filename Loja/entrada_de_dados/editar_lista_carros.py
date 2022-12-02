from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivo, \
    tirar_espacos_e_maiusculas
from estrutura import Loja
from estrutura.Carro import Carro


def salvar_carro_em_lista(carro: Carro, loja: Loja):
    endereco_do_arquivo = "entrada_de_dados/lista_carros"

    escrever = _escrever_objeto_carro(carro, loja)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_objeto_carro(carro: Carro, loja: Loja):
    montadora_do_carro = tirar_espacos_e_maiusculas(carro.montadora)
    nome_do_carro = tirar_espacos_e_maiusculas(carro.nome)

    variavel_da_classe = f'carro_{montadora_do_carro}_{nome_do_carro}_{carro.codigo}'
    classe = 'Carro(montadora, nome, ano, valor_de_aquisicao, codigo_de_registro)'

    return f'' \
           f'{carro.mostrar_atributos_principais()}' \
           f'{variavel_da_classe} = {classe}\n' \
           f'add_carro_na_lista({variavel_da_classe}, "{variavel_da_classe}", {int(loja.cnpj)})' \
           f'\n'

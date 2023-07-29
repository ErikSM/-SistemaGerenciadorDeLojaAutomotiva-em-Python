from entrada_de_dados.funcoes_de_edicao import abrir_modificar_e_salvar_arquivos_em_geral
from estrutura.Venda import Venda
from estrutura.Carro import Carro


def adicionar_venda_em_lista(venda: Venda):
    endereco_do_arquivo = "entrada_de_dados/lista_vendas"

    formato = "py"

    escrever = _escrever_venda(venda)

    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_venda(venda: Venda):
    variavel_da_classe = f'venda_{venda.codigo}'
    return f'\n' \
           f'{venda}' \
           f'\n' \
           f'add_venda_na_lista({variavel_da_classe})\n\n' \
           f'\n' \
           f'# -------------------------------------------------------' \
           f'\n'


def remover_carro_vendido_da_lista_carros(carro: Carro, codigo):
    endereco_do_arquivo = "entrada_de_dados/lista_carros"

    formato = "py"

    escrever = _escrever_remocao_de_carro_vendido(carro, codigo)

    abrir_modificar_e_salvar_arquivos_em_geral(endereco_do_arquivo, formato, escrever)


def _escrever_remocao_de_carro_vendido(carro: Carro, codigo):
    return f'\n' \
           f'remover_carro_da_lista({carro}, "{codigo}")' \
           f'\n'

from entrada_de_dados.salvar_modificacoes_no_arquivo import abrir_modificar_e_salvar_arquivo
from estrutura.Venda import Venda
from estrutura.Carro import Carro


def adicionar_relatorio_de_venda_em_lista_do_main(venda: Venda):
    endereco_do_arquivo = "entrada_de_dados/lista_de_vendas_efetuadas"

    escrever = _escrever_venda(venda)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_venda(venda: Venda):
    venda = venda
    return f'\n' \
           f'{venda}' \
           f'\n' \
           f'add_venda_na_lista_do_main(venda_{venda.codigo})\n\n' \
           f'\n' \
           f'# -------------------------------------------------------\n' \
           f'\n'


def remover_carro_vendido_da_lista_de_carros_registrados(carro: Carro, codigo):
    endereco_do_arquivo = "entrada_de_dados/lista_de_carros_registrados"

    escrever = _escrever_remocao_de_carro_vendido(carro, codigo)

    abrir_modificar_e_salvar_arquivo(endereco_do_arquivo, escrever)


def _escrever_remocao_de_carro_vendido(carro: Carro, codigo):
    return f'\n' \
           f'remover_carro_da_lista({carro}, "{codigo}")' \
           f'\n'

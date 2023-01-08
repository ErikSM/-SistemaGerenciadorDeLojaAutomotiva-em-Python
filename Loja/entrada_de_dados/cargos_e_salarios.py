# profissao = {"cargo": cargo, "salario": salario, "bonus": bonus, "comissao": comissao}
# dict_loja[cnpj] = { dict_cargos[cargo]: profissao }
dicionario_de_cargos = dict()
dicionario_de_cargos_da_loja = dict()


def _atualizar_dicionario_de_cargos_da_loja(cnpj):
    dicionario_de_cargos_da_loja[cnpj] = dicionario_de_cargos


def _adicinar_profissao_em_dicionario_de_cargos(profissao):
    dicionario_de_cargos[f'{profissao["cargo"]}'] = profissao


def criar_profissao(cargo, salario, bonus, comissao, cnpj, linha_no_arquivo):
    profissao = {"cargo": cargo, "salario": salario,
                 "bonus": bonus, "comissao": comissao, "linha no arquivo": linha_no_arquivo}
    _adicinar_profissao_em_dicionario_de_cargos(profissao)
    _atualizar_dicionario_de_cargos_da_loja(cnpj)


# ----------------  -------------   --------------------  ---------------


# gerente
nome = "gerente"
salario = "5000"
bonus = 0.25
comissao = 0.07
cnpj = "124134100000"
linha = 25
criar_profissao(nome, salario, bonus, comissao, cnpj, linha)


# venededor
nome = "vendedor"
salario = "1200"
bonus = 0.10
comissao = 0.05
cnpj = "124134100000"
linha = 35
criar_profissao(nome, salario, bonus, comissao, cnpj, linha)


# secretaria
nome = "secretaria"
salario = "1500"
bonus = 0.10
comissao = 0
cnpj = "124134100000"
linha = 45
criar_profissao(nome, salario, bonus, comissao, cnpj, linha)


# zelador
nome = "zelador"
salario = "zelaror"
bonus = 0
comissao = 0
cnpj = "124134100000"
linha = 55
criar_profissao(nome, salario, bonus, comissao, cnpj, linha)


# advogado    
nome = "advogado"    
sarario = "6000"    
bonus = 0.0    
comissao = 0.0    
cnpj = "124134100000"    
linha = 65
criar_profissao(nome, salario, bonus, comissao, cnpj, linha)    


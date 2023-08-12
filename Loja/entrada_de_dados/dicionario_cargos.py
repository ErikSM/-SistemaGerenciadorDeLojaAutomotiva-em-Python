from estrutura.Cargo import Cargo

dicionario_de_cargos = dict()
dicionario_de_cargos_da_loja = dict()


def _atualizar_dicionario_de_cargos_da_loja(cnpj_da_loja):
    dicionario_de_cargos_da_loja[cnpj_da_loja] = dicionario_de_cargos


def _adicinar_profissao_em_dicionario_de_cargos(profissao, cnpj_da_loja):
    dicionario_de_cargos[f'{profissao["cargo"]} {cnpj_da_loja}'] = profissao


def criar_profissao(cargo: Cargo, linha_no_arquivo):
    profissao = {"cargo": cargo.nome, "salario": cargo.salario,
                 "bonus": cargo.bonus, "comissao": cargo.comissao,
                 "linha no arquivo": linha_no_arquivo, "cnpj": cargo.cnpj}

    _adicinar_profissao_em_dicionario_de_cargos(profissao, cargo.cnpj)
    _atualizar_dicionario_de_cargos_da_loja(cargo.cnpj)


# ----------------  -------------   --------------------  ---------------


# loja criada
dicionario_de_cargos_da_loja["124134100000"] = dict()


# gerente
nome = "gerente"
salario = "5000"
bonus = 0.25
comissao = 0.07
cnpj = "124134100000"
linha = 31
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# vendedor
nome = "vendedor"
salario = "1200"
bonus = 0.10
comissao = 0.05
cnpj = "124134100000"
linha = 41
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# secretaria
nome = "secretaria"
salario = "1500"
bonus = 0.10
comissao = 0.0
cnpj = "124134100000"
linha = 51
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# zelador
nome = "zelador"
salario = "1200"
bonus = 0.0
comissao = 0.0
cnpj = "124134100000"
linha = 61
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# advogado
nome = "advogado"
salario = "6500"
bonus = 0.01
comissao = 0.0
cnpj = "124134100000"
linha = 71
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# loja criada
dicionario_de_cargos_da_loja["823765760000"] = dict()


# gerente
nome = "gerente"
salario = "8000"
bonus = 0.08
comissao = 0.01
cnpj = "823765760000"
linha = 85
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# vendedor    
nome = "vendedor"    
salario = "1200"    
bonus = 0.3    
comissao = 1.2    
cnpj = "823765760000"    
linha = 95
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)    


# loja criada    
dicionario_de_cargos_da_loja["2342"] = dict()    


# loja criada    
dicionario_de_cargos_da_loja["2342"] = dict()    


# loja criada    
dicionario_de_cargos_da_loja["43217051000182"] = dict()    


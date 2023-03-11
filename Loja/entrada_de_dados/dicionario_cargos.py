from estrutura.Cargo import Cargo

dicionario_de_cargos = dict()
dicionario_de_cargos_da_loja = dict()


def _atualizar_dicionario_de_cargos_da_loja(cnpj):
    dicionario_de_cargos_da_loja[cnpj] = dicionario_de_cargos


def _adicinar_profissao_em_dicionario_de_cargos(profissao, cnpj):
    dicionario_de_cargos[f'{profissao["cargo"]} {cnpj}'] = profissao


def criar_profissao(cargo: Cargo, linha):
    profissao = {"cargo": cargo.nome, "salario": cargo.salario,
                 "bonus": cargo.bonus, "comissao": cargo.comissao,
                 "linha no arquivo": linha, "cnpj": cargo.cnpj}
    _adicinar_profissao_em_dicionario_de_cargos(profissao, cargo.cnpj)
    _atualizar_dicionario_de_cargos_da_loja(cargo.cnpj)


# ----------------  -------------   --------------------  ---------------


# loja criada
dicionario_de_cargos_da_loja["124134100000"] = None


# gerente
nome = "gerente"
salario = "5000"
bonus = 0.25
comissao = 0.07
cnpj = "124134100000"
linha = 30
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# vendedor
nome = "vendedor"
salario = "1200"
bonus = 0.10
comissao = 0.05
cnpj = "124134100000"
linha = 40
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# secretaria
nome = "secretaria"
salario = "1500"
bonus = 0.10
comissao = 0.0
cnpj = "124134100000"
linha = 50
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# zelador
nome = "zelador"
salario = "1200"
bonus = 0.0
comissao = 0.0
cnpj = "124134100000"
linha = 60
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# advogado
nome = "advogado"
salario = "6500"
bonus = 0.01
comissao = 0.0
cnpj = "124134100000"
linha = 70
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


# loja criada    
dicionario_de_cargos_da_loja["823765760000"] = None


# gerente    
nome = "gerente"    
salario = "8000"    
bonus = 0.08    
comissao = 0.01    
cnpj = "823765760000"
linha = 84    
criar_profissao(Cargo(nome, salario, bonus, comissao, cnpj), linha)


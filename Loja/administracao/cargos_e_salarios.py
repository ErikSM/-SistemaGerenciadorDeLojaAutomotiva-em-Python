dicionario_de_cargos = dict()


def criar_profissao(cargo, salario, bonus, comissao):
    profissao = {"cargo": cargo, "salario": salario,
                 "bonus": bonus, "comissao": comissao}
    _adicinar_profissao_em_dicionario_de_cargos(profissao)


def _adicinar_profissao_em_dicionario_de_cargos(profissao):
    dicionario_de_cargos[f"{profissao['cargo']}"] = profissao


# ----------------------  ----------------  -------------   ---------


# Gerente
nome_cargo_gerente = "gerente"
salario_gerente = "5000"
bonus_gerente = 0.25
comissao_gerente = 0.07

criar_profissao(nome_cargo_gerente, salario_gerente,
                bonus_gerente, comissao_gerente)

# Venededor
nome_cargo_vendedor = "vendedor"
salario_vendedor = "1200"
bonus_vendedor = 0.10
comissao_vendedor = 0.05

criar_profissao(nome_cargo_vendedor, salario_vendedor,
                bonus_vendedor, comissao_vendedor)

# Secretaria
nome_cargo_secretaria = "secretaria"
salario_secretaria = "1500"
bonus_secretaria = 0.10
comissao_secretaria = 0

criar_profissao(nome_cargo_secretaria, salario_secretaria,
                bonus_secretaria, comissao_secretaria)

# Zelador
nome_cargo_zelador = "zelador"
salario_zelador = "zelaror"
bonus_zelador = 0
comissao_zelaor = 0

criar_profissao(nome_cargo_zelador, salario_zelador,
                bonus_zelador, comissao_zelaor)

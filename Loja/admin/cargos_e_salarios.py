salario_gerente = "5000"
salario_vendedor = "1200"

bonus_gerente = 0.25
bonus_vendedor = 0.10

comissao_gerente = 0
comissao_vendedor = 0.05

gerente = {"funcao": "Gerente", "salario": salario_gerente, "bonus": bonus_gerente, "comissao": comissao_gerente}
vendedor = {"funcao": "vendedor", "salario": salario_vendedor, "bonus": bonus_vendedor, "comissao": comissao_vendedor}

dicio_de_cargos = dict()
dicio_de_cargos["gerente"] = gerente
dicio_de_cargos["vendedor"] = vendedor
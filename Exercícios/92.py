trabalhador = {}
trabalhador["Nome"] = str(input("Nome: "))
nascimento = int(input("Ano de Nascimento: "))
trabalhador["Idade"] = 2024 - nascimento
trabalhador["CPTS"] = int(input("Carteira de Trabalho (0 não tem): "))

if trabalhador["CPTS"] > 0:
    trabalhador["Contratação"] = int(input("Ano da Contratação: "))
    trabalhador["Salário"] = float(input("Salário: R$"))
    trabalhador["Aposentadoria"] = trabalhador["Idade"] + (trabalhador["Contratação"] + 35) - 2024 

for c, v in trabalhador.items():
    print(f"{c} tem o valor {v}.")
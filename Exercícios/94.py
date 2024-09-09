pessoas = {}                  
lista = []                    
cadastradas = 0
soma = 0
média = 0

while True:
    pessoas["Nome"] = str(input("Nome: "))
    pessoas["Sexo"] = str(input("Sexo [M/F]: "))

    while pessoas["Sexo"] not in 'MmFf':
        pessoas["Sexo"] = str(input("Erro! Por favor, digite apenas M ou F: "))
    
    pessoas["Idade"] = int(input("Idade: "))
    lista.append(pessoas.copy())
    cadastradas += 1
    soma += pessoas["Idade"]
    média = soma / cadastradas

    continuar = str(input("Quer continuar [S/N]? "))

    if continuar in 'Nn':
        break

    while continuar not in 'SsNn':
        continuar = str(input("Erro! Por favor, digite apenas S ou N: "))
        if continuar in 'Nn':
            break

print(f"Ao todo temos, {cadastradas} pessoas cadastradas.")
print(f"A média de idade é de {média:5.2f} anos.")
print(f"As mulheres cadastradas foram: ", end = '')

for p in lista:
    if p["Sexo"] in 'Ff':
        print(f"{p["Nome"]} ", end = '')
print()

print(f"Lista de pessoas com idade acima da média: ", end = '')

for am in lista:
    if am["Idade"] > média:
        print(f"{am["Nome"]} ", end = '')
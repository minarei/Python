salário = float(input("Qual é o salário do funcionário? R$"))

if salário > 1250:
    aumento = salário * 1.10
elif salário <= 1250:
    aumento = salário * 1.15

print("Quem ganhava R${:.2f} reais, com o aumento passará a ganhar R${:.2f} reais." .format(salário, aumento))
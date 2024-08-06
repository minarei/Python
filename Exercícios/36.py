casa = float(input("Qual o valor da casa? R$"))
salário = float(input("Qual o salário do comprador? R$"))
anos = int(input("Quantos anos de financiamento? "))
prestação = casa / (anos * 12)

print("Para pagar uma casa de R${:.2f} reais em {} anos, a prestação será de R${:.2f} reais." .format(casa, anos, prestação))

if prestação > salário * 30 / 100:
    print("O empréstimo foi negado!")
else:
    print("O empréstimo pode ser concedido!")
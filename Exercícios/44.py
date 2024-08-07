preço = float(input("Preço das compras: R$"))

print("Formas de pagamento: ")
print("[ 1 ] - À vista no dinheiro ou cheque")
print("[ 2 ] - À vista no cartão")
print("[ 3 ] - 2x no cartão")
print("[ 4 ] - 3x ou mais no cartão")
opção = int(input("Sua opção: "))

if opção == 1:
    desconto = preço * 0.90
    print("Sua compra de R${:.2f} reais, sairá R${:.2f} reais com 10% de desconto à vista no dinheiro ou cheque." .format(preço, desconto))
elif opção == 2:
    desconto = preço * 0.95
    print("Sua compra de R${:.2f} reais, sairá R${:.2f} reais com 5% de desconto à vista no cartão." .format(preço, desconto))
elif opção == 3:
    parcelas = preço / 2
    print("Sua compra de R${:.2f} reais, será paga com duas parcelas de R${:.2f} reais." .format(preço, parcelas))
elif opção == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = preço + (preço * 0.20)
    print("Sua compra será parcelada em {}x de R${:.2f} com juros." .format(parcelas, juros))
    print("Sua compra de R${:.2f} reais irá custar, no final, R${:.2f} reais." .format(preço, juros / parcelas))
else:
    print("Opção inválida!. Tente novamente.")
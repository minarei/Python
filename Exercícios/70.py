print("=" * 14)
print("     Loja     ")
print("=" * 14)
soma = 0
produto1000 = 0
barato = 0
produtob = ' '
cont = 0

while True:
    produto = str(input("Nome do Produto: ")).strip()
    preço = float(input("Preço: R$"))
    continuar = ' '
    soma += preço
    cont += 1

    if preço > 1000:
        produto1000 += + 1

    if cont == 1 or preço < barato:
        barato = preço
        produtob = produto

    while continuar not in 'SsNn':
        continuar = str(input("Quer continuar? [S/N] ")).strip()[0]
    
    if continuar in 'Nn':
        break
print(f"O total da compra foi R${soma} reais.")
print(f"Temos {produto1000} produtos custando mais de R$1000.00 reais.")
print(f"O produto mais barato foi {produtob} e custa R${barato} reais.")
pre = float(input("Qual o preço do produto? R$"))
nov = pre - (pre * 5 / 100)

print("O produto que custava R${:.2f}, na promoção com 5% de desconto vai custar R${:.2f}" .format(pre, nov))
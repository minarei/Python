d = float(input("Qual a distância da sua viagem? "))

print("Você está prestes a começar uma viagem de {:.1f}km." .format(d))

if d <= 200:
    p = d * 0.50
    print("E o preço da sua viagem será de R${:.2f} reais." .format(p))
else:
    p = d * 0.45
    print("E o preço da sua viagem será de R${:.2f} reais." .format(p))
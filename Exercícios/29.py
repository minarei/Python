v = float(input("Qual a velocidade do carro? "))
k = (v - 80) * 7

if v > 80:
    print("Multado! Você excedeu o limite de velocidade permitido que é de 80km/h.")
    print("Você deve pagar uma multa de R${:.2f} reais." .format(k))
    print("Tenha um bom dia e dirija com segurança!")
else:
    print("Tenha um bom dia e dirija com segurança!")
s = float(input("Qual o salário do funcionário? R$"))
n = s + (s * 15 / 100)

print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passará a ganhar R${:.2f}" .format(s, n))
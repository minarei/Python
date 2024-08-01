c = int(input("Por quantos dias o carro foi alugado? "))
q = float(input("Quantos foram os quilômetros rodados? "))
p = (c * 60) + (q * 0.15)

print("O total a pagar é de R${:.2f}." .format(p))
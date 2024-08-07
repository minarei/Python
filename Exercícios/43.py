peso = float(input("Qual é o seu peso em quilos? "))
altura = float(input("Qual é a sua altura? "))
imc = peso / altura**2

print("O IMC dessa pessoa é de {:.1f}." .format(imc))

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif imc >= 18.5 and imc <= 25:
    print("Você está no peso ideal!")
elif imc >= 26 and imc <= 30:
    print("Você está em sobrepeso.")
elif imc >= 31 and imc <= 40:
    print("Você está na obesidade.")
else:
    print("Você está na obesidade mórbida.")
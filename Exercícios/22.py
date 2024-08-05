n = str(input("Digite o seu nome completo: ")).strip()
s = n.split()

print("Analisando seu nome...")
print("Seu nome em letras maiúsculas: {}" .format(n.upper()))
print("Seu nome em letras minúsculas: {}" .format(n.lower()))
print("Seu nome tem ao todo {} letras." .format(len(n) - n.count(' ')))
print("Seu primeiro nome é {} e ele tem {} letras." .format(n[0], len(s[0])))
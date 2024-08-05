n = str(input("Digite seu nome completo: ")).strip()
c = n.split()

print("Muito prazer em te conhecer!")
print("Seu primeiro nome é {}." .format(c[0]))
print("Seu último nome é {}." .format(c[len(c)-1]))
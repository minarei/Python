a = int(input("Digite um ano para saber se o mesmo é bissexto: "))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("O ano {} é bissexto." .format(a))
elif a == 0:
    print("O ano 2024 é bissexto.")
else:
    print("O ano {} não é bissexto." .format(a))
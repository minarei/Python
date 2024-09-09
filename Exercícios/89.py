lista1 = []
lista2 = []

while True:
    nome = str(input("Nome: "))
    lista2.append(nome)
    nota1 = int(input("Nota 1: "))
    lista2.append(nota1)
    nota2 = int(input("Nota 2: "))
    lista2.append(nota2)
    lista1.append(lista2.copy())
    lista2.clear()
    média = (nota1 + nota2) / 2

    continuar = str(input("Quer continuar? [S/N]: "))

    if continuar in 'Nn':
        break

print(lista1)

while True:
    notas = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    print(f"As notas de {lista1[notas][0]} são {lista1[notas][1]} e {lista1[notas][2]}.")

    if notas == 999:
        print("Finalizando...")
        break
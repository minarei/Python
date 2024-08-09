from time import sleep

primeiro = int(input("Primeiro valor: "))
segundo = int(input("Segundo valor: "))
maior = 0
opção = 0

while opção != 5:
    print("[ 1 ] - Somar")
    print("[ 2 ] - Multiplicar")
    print("[ 3 ] - Maior")
    print("[ 4 ] - Novos Números")
    print("[ 5 ] - Sair do programa")
    opção = int(input("Qual sua opção? "))

    if opção == 1:
        soma = primeiro + segundo
        print(f"A soma entre {primeiro} e {segundo} vale {soma}.")
    elif opção == 2:
        multiplicação = primeiro * segundo
        print(f"A multiplicação entre {primeiro} e {segundo} vale {multiplicação}.")
    elif opção == 3:
        if primeiro > segundo:
            maior = primeiro
            print(f"O número {maior} é maior que o segundo.")
        elif segundo > primeiro:
            maior = segundo
            print(f"O número {maior} é maior que o primeiro.")
        else:
            print("Os números são iguais.")
    elif opção == 4:
        primeiro = int(input("Primeiro valor: "))
        segundo = int(input("Segundo valor: "))
    elif opção == 5:
        print("Saindo do programa...")
        sleep(1.5)
        break
    else:
        print("Opção inválida. Tente novamente.")
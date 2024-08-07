from random import randint

print("Suas opções: ")
print("[ 0 ] - Pedra")
print("[ 1 ] - Papel")
print("[ 2 ] - Tesoura")

jogada = int(input("Qual sua jogada? "))
lista = ['Pedra', 'Papel', 'Tesoura']
escolha = randint(0, 2)

if escolha == 0:
    if jogada == 0:
        print("Jogada inválida.")
    elif jogada == 1:
        print("O jogador venceu!")
    elif jogada == 2:
        print("O computador venceu!")
elif escolha == 1:
    if jogada == 0:
        print("O computador venceu!")
    elif jogada == 1:
        print("Jogada inválida!")
    elif jogada == 2:
        print("O jogador venceu!")
elif escolha == 2:
    if jogada == 0:
        print("O jogador venceu!")
    elif jogada == 1:
        print("O computador venceu!")
    elif jogada == 2:
        print("Jogada inválida.")
else:
    print("Jogada inválida. Tente novamente.")
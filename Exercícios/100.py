from random import randint
from time import sleep

números = []

def sorteia():
    print("Sorteando os valores da lista: ", end = '')
    for valores in range(0, 5):
        valores = randint(1, 10)
        print(f"{valores} ", end = '', flush = True)
        sleep(0.2)

        if valores % 2 == 0:
            números.append(valores)

def somapar():
    soma = 0
    for pares in números:
        if pares % 2 == 0:
            soma += pares
    print(f"\nSomando os pares de {números}, temos {soma}.", end = '')

sorteia()
somapar()
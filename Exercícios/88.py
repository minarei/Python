from random import sample
from time import sleep

lista = list(range(1, 60))
jogos = int(input(("Quantos jogos você quer que eu sorteie? ")))

for j in range(1, jogos + 1):
    bilhete = sample(lista, 6)
    bilhete.sort()
    print(f"Jogo {j}: {bilhete}")
    sleep(0.5)
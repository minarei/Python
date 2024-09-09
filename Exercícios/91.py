from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'Jogador1': randint(1, 6), 'Jogador2': randint(1, 6), 'Jogador3': randint(1, 6), 'Jogador4': randint(1, 6)}
ranking = {}

print("Valores sorteados: ")

for c, v in jogadores.items():
    print(f"O {c} tirou {v} no dado.")
    sleep(0.5)

ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)

print("Ranking: ")

for i, v in enumerate(ranking):
    print(f"{i + 1}° lugar: O {v[0]} tirou {v[1]} no dado.")
    sleep(0.5)
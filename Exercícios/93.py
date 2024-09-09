jogador = {}
partidas = []
soma = 0
jogador["nome"] = str(input("Nome do Jogador: "))
jogos = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))

for c in range(0, jogos):
    gols = int(input(f"Quantos gols na partida {c}? "))
    soma += gols
    partidas.append(gols)

jogador["gols"] = partidas
jogador["total"] = soma

print("=" * 45)
print(jogador)
print("=" * 45)

for k, v in jogador.items():
    print(f"O campo {k} possui o valor {v}.")

print("=" * 45)
print(f"O jogador {jogador["nome"]} jogou {jogos} partidas.")

for k, v in enumerate(jogador["gols"]):
    print(f"=> Na partida {k}, fez {v} gols.")

print(f"Foi um total de {soma} gols.")
print("=" * 45)
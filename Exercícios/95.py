jogador = {}
time = []
partidas = []
soma = 0

while True:
    jogador.clear()
    jogador["nome"] = str(input("Nome do Jogador: "))
    jogos = int(input(f"Quantas partidas {jogador["nome"]} jogou? "))
    partidas.clear()

    for c in range(0, jogos):
        partidas.append(int(input(f"Quantos gols na partida {c}? ")))

    jogador["gols"] = partidas.copy()
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())

    while True:
        continuar = str(input("Quer continuar? [S/N] ")).upper()[0]

        if continuar in 'SN':
            break
        print("Erro! Apenas sim (S) ou não (N).")

    if continuar in 'N':
        break

print("cod")

for i in jogador.keys():
    print(f"{i:<15}", end = '')
print()

for k, v in enumerate(time):
    print(f"{k:>4}", end = '')
    for d in v.values():
        print(f"{str(d):<15}", end = '')
    print()

while True:
    dados = int(input("Mostrar dados de qual jogador? (999 interrompe) "))

    if dados == 999:
        break

    if dados >= len(time):
        print("Erro! Não existe jogador com o código da busca.")
    else:
        print(f"Levantamento do jogador {time[dados]["nome"]}: ")
        for k, v in enumerate(time[dados]["gols"]):
            print(f"No jogo {k + 1}, ele fez {v} gols.")
def ficha(jogador = "<desconhecido>", número = 0):
    return print(f"O jogador {jogador} fez {número} gols no campeonato.")

nome = str(input("Nome do Jogador: "))
gols = str(input("Número de Gols: "))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(número = gols)
else:
    ficha(nome, gols)
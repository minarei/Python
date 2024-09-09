times = ('Corinthians', 'Palmeiras', 'Santos', 'São Paulo', 'Flamengo', 'Fluminense', 'Vasco da Gama', 'Botafogo', 'Cruzeiro', 'Atlético-MG', 'Internacional', 'Grêmio', 'Athletico-PR', 'Coritiba', 'Bahia', 'Goiás', 'Vitória', 'Sport Recife', 'América-MG', 'Juventude')

print(f"Os 5 primeiros são: {times[0:5]}")
print(f"Os 4 últimos são: {times[-5:-1]}")
print(f"Times em ordem alfabética: {sorted(times)}")
print(f"O Botafogo está na {times.index('Botafogo')}ª posição.")
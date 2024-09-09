from random import randint

c = 0
ma = 0
me = 0
t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f"Os valores sorteados foram: {t}")
print(f"O maior valor sorteado foi: {max(t)}")
print(f"O menor valor sorteado foi: {min(t)}")
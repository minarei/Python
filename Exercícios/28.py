from time import sleep
from random import randint

print("-=" * 30)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")

r = randint(0, 5)
n = int(input("Em que número eu pensei? "))
print("Processando...")
sleep(3)

if n == r:
    print("Você pensou {} e eu pensei {}." .format(n, r))
    print("Parabéns! Você ganhou de mim.")
else:
    print("Você pensou {} e eu pensei {}." .format(n, r))
    print("Eu venci! Tente novamente.")

print("-=" * 30)
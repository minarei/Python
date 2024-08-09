from random import randint

print("Sou seu computador e acabei de pensar num número entre 1 e 10.")
print("Será que você consegue adivinhar qual foi? ")

p = int(input("Qual seu palpite? "))
r = randint(0, 10)
t = 0

while p != r:
    t = t + 1
    if p > r:
        p = int(input("Menos. Tente novamente: "))
    else:
        p = int(input("Mais. Tente novamente: "))

print(f"Acertou com {t} tentativas. Parabéns!")
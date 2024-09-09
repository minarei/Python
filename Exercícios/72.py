t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input("Digite um número entre 0 e 20: "))

while n > 20:
    n = int(input("Número inválido. Digite novamente: "))

print(f"Você digitou o número {t[n]}.")
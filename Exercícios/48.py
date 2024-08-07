s = 0

for n in range(1, 500, 2):
    if n % 3 == 0:
        s = s + n

print("A soma de todos os valores é {}." .format(s))
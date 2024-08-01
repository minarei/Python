from math import sqrt

c = float(input("Comprimento do cateto oposto: "))
a = float(input("Comprimento do cateto adjacente: "))

f = c**2 + a**2

print("A hipotenusa vai medir {:.2f}." .format(sqrt(f)))

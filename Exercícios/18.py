from math import sin, cos, tan, radians

a = float(input("Qual o ângulo que você deseja: "))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print("O ângulo {} tem o seno de {:.2f}." .format(a, s))
print("O ângulo {} tem o cosseno de {:.2f}." .format(a, c))
print("O ângulo {} tem a tangente de {:.2f}." .format(a, t))
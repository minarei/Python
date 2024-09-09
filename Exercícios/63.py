print("~" * 22)
print("Sequência de Fibonacci")
print("~" * 22)

t = int(input("Quantos termos você deseja mostrar? "))
t1 = 0
t2 = 1
c = 3
print(f"{t1} -> {t2} -> ", end = '')

while c <= t:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f"{t3} -> ", end ='')
    c = c + 1

print("Acabou!")
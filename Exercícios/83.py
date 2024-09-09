l = []
e = str(input("Digite uma expressão: "))

for s in e:
    if s == "(":
        l.append("(")
    elif s == ")":
        if len(l) > 0:
            l.pop()
        else:
            l.append(")")
            break

if len(e) == 0:
    print("Sua expressão está válida.")
else:
    print("Sua expressão está inválida.")
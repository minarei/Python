a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

men = a
mai = a

if b < a and c < a:
    men = b
elif c < a and c < b:
    men = c


if b > a and b > c:
    mai = b
elif c > a and c > b:
    mai = c

print("O maior valor digitado foi {}." .format(mai))
print("O menor valor digitado foi {}." .format(men))
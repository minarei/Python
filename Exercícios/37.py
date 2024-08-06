inteiro = int(input("Digite um número inteiro qualquer: "))

print("Escolha uma das bases abaixo para conversão: ")
print("[ 1 ] - Binário")
print("[ 2 ] - Octal")
print("[ 3 ] - Hexadecimal")

bases = int(input("Sua opção: "))

if bases == 1:
    print("{} convertido para binário é igual a {}." .format(inteiro, bin(inteiro)))
elif bases == 2:
    print("{} convertido para octal é igual a {}" .format(inteiro, oct(inteiro)))
elif bases == 3:
    print("{} convertido para hexadecimal é igual a {}." .format(inteiro, hex(inteiro)))
else:
    print("Valor inválido! Tente novamente.")
from utilidades import módulo107

preço = float(input("Digite o preço: R$"))
print(f"A metade de {preço} é {módulo107.metade(preço)}.")
print(f"O dobro de {preço} é {módulo107.dobro(preço)}.")
print(f"Aumentando 10% de {preço}, temos {módulo107.aumento(preço):.2f}.")
print(f"Reduzindo 10% de {preço}, temos {módulo107.redução(preço):.2f}.")
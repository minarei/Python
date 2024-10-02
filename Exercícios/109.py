from utilidades import módulo109

preço = float(input("Digite o preço: "))
print(f"A metade de {módulo109.moeda(preço)} é {módulo109.metade(preço, True)}.")
print(f"O dobro de {módulo109.moeda(preço)} é {módulo109.dobro(preço, False)}.")
print(f"Aumentando 10% de {módulo109.moeda(preço)}, temos {módulo109.aumento(preço, True)}.")
print(f"Reduzindo 10% de {módulo109.moeda(preço)}, temos {módulo109.redução(preço, False)}.")
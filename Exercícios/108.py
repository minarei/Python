from utilidades import módulo108

preço = float(input("Digite o preço: "))
print(f"A metade de {módulo108.moeda(preço)} é {módulo108.moeda(módulo108.metade(preço))}.")
print(f"O dobro de {módulo108.moeda(preço)} é {módulo108.moeda(módulo108.dobro(preço))}.")
print(f"Aumentando 10% de {módulo108.moeda(preço)}, temos {módulo108.moeda(módulo108.aumento(preço))}.")
print(f"Reduzindo 10% de {módulo108.moeda(preço)}, temos {módulo108.moeda(módulo108.redução(preço))}.")
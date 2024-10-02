def metade(n = 0, format = False):
    resultado = n / 2
    return resultado if format is False else moeda(resultado)

def dobro(n = 0, format = False):
    resultado = n * 2
    return resultado if format is False else moeda(resultado)

def aumento(n = 0, a = 0, format = False):
    resultado = n + (n * a / 100)
    return resultado if format is False else moeda(resultado)

def redução(n = 0, d = 0, format = False):
    resultado = n - (n * d / 100)
    return resultado if format is False else moeda(resultado)

def moeda(n = 0, moeda = 'R$'):
    return f"{moeda}{n:.2f}".replace(".", ",")

def linha():
    print("-=" * 12)

def resumo(n = 0, a = 0, d = 0):
    linha()
    print("    Resumo do Valor     ")
    linha()
    print(f"Preço analisado:    {moeda(n)}")
    print(f"Dobro do preço:     {moeda(dobro(n))}")
    print(f"Metade do preço:    {moeda(metade(n))}")
    print(f"{a}% de aumento:    {moeda(aumento(n, a))}")
    print(f"{d}% de desconto:   {moeda(redução(n, d))}")
    linha()
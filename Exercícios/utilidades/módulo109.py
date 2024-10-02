def metade(n = 0, format = False):
    resultado = n / 2
    return resultado if format is False else moeda(resultado)

def dobro(n = 0, format = False):
    resultado = n * 2
    return resultado if format is False else moeda(resultado)

def aumento(n = 0, format = False):
    resultado = n * 1.10
    return resultado if format is False else moeda(resultado)

def redução(n = 0, format = False):
    resultado = n * 0.90
    return resultado if format is False else moeda(resultado)

def moeda(n = 0, moeda = 'R$'):
    return f"{moeda}{n:.2f}".replace(".", ",")
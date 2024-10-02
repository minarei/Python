def metade(n = 0):
    return n / 2

def dobro(n = 0):
    return n * 2

def aumento(n = 0):
    return n * 1.10

def redução(n = 0):
    return n * 0.90

def moeda(n = 0, moeda = 'R$'):
    return f"{moeda}{n:.2f}".replace(".", ",")
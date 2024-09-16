def fatorial(número, show = False):
    """
    Calcula o fatorial de um número.
    -> n: número a ser calculado.
    -> show: mostrar a conta ou não (opcional).
    -> return: retorna o valor fatorial de um número n.
    """
    f = 1
    for n in range(número, 0, -1):
        if show:
            print(n, end = '')
            if n > 1:
                print(" x ", end = '')
            else:
                print(" = ", end = '')
        f *= n
    return f

print(fatorial(6, show = False))
help(fatorial)
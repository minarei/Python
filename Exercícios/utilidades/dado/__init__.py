def leiaDinheiro(p):
    válido = False
    while not válido:
        entrada = str(input(p)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro! "{entrada}" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)
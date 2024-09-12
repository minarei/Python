print("Controle de Terrenos")
print()

def área(l, c):
    á = l * c
    print(f"A área de um terreno {l}x{c} é de {á}m².")

largura = float(input("Largura: "))
comprimento = float(input("Comprimento: "))

área(largura, comprimento)
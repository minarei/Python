print("-=" * 30)
print("Analisador de Triângulos")
print("-=" * 30)
primeiro = float(input("Primeiro segmento: "))
segundo = float(input("Segundo segmento: "))
terceiro = float(input("Terceiro segmento: "))

if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print("Os valores citados podem formar um triângulo!")
else:
    print("Os valores citados não podem formar um triângulo!")
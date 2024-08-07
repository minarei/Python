primeiro = float(input("Primeiro segmento: "))
segundo = float(input("Segundo segmento: "))
terceiro = float(input("Terceiro segmento: "))

if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    if primeiro != segundo != terceiro != primeiro:
        print("Os valores citados podem formar um triângulo do tipo escaleno!")
    elif primeiro == segundo == terceiro:
        print("Os valores citados podem formar um triângulo do tipo equilátero!")
    else :
        print("Os valores citados podem formar um triãngulo do tipo isósceles!")
else:
    print("Os valores citados não formam um triângulo!")
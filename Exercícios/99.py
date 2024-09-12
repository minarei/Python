from time import sleep

def linha():
    print("-=" * 30)

linha()

def maior(*números):
    contador = 0
    maior = 0
    print("Analisando os números passados...")
    for n in números: 
        print(f"{n} ", end = '', flush = True)
        sleep(0.2)
        contador += 1

        if contador == 0:
            maior = n
        else:
            if n > maior:
                maior = n

    print(f"\nForam informados ao todo {contador} valores.")
    print(f"O maior valor informado foi {maior}.")

maior(2, 9, 4, 5, 7, 1)
linha()
maior(4, 7, 8)
linha()
maior(1, 2)
linha()
maior(6)
linha()
maior(0)
linha()
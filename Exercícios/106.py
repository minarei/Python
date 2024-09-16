from time import sleep

def sistema():
    print("=" * 25)
    print(" Sistema de Ajuda PYHelp ")
    print("=" * 25)

    comando = str(input("Função ou Biblioteca: "))
    print(f"Acessando o manual do comando {comando}")
    sleep(0.3)
    help(comando)

sistema()
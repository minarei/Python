def leiaInt():
    global inteiro
    while True:
        try:
            inteiro = int(input("Digite um número inteiro: "))
        except (KeyboardInterrupt):
            print("\n\033[31mO usuário preferiu não digitar um número inteiro.\033[m")
            inteiro = 0
            break
        except:
            print("\033[31mErro! Por favor, digite um número inteiro valido.\033[m")
        else:
            break

def leiaFloat():
    global real
    while True:
        try:
            real = float(input("Digite um número real: "))
        except (KeyboardInterrupt):
            print("\n\033[31mO usuário preferiu não digitar um número real.\033[m")
            real = 0
            break
        except:
            print("\033[31mErro! Por favor, digite um número real válido.\033[m")
        else:
            break

leiaInt()
leiaFloat()
print(f"O valor inteiro digitado foi {inteiro} e o real foi {real}.")
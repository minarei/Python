def linha():
    print("=" * 30)

def principal(texto):
    global opção
    global lista
    lista = []
    while True:
        linha()
        print(texto.center(30))
        linha()
        print("\033[33m1 - \033[34mVer pessoas cadastradas\033[m")
        print("\033[33m2 - \033[34mCadastrar nova pessoa\033[m")
        print("\033[33m3 - \033[34mSair do sistema\033[m")
        linha()
        try:
            opção = int(input("\033[33mSua opção: \033[m"))
            opções()
            if opção > 3 or opção < 1:
                print("\033[31mErro! Por favor, digite uma opção válida.\033[m")
            elif opção == 3:
                break
        except (ValueError):
            print("\033[31mErro! Por favor, digite um número inteiro válido!\033[m")
        except (KeyboardInterrupt):
            print("\033[31mO usuário preferiu não digitar a opção.\033[m")
            break

def opções():
    match opção:
        case 1:
            linha()
            print(f"Pessoas Cadastradas".center(30))
            print()
            lerArquivo("arquivos.txt")
            linha()
        case 2:
            linha()
            print(f"Novo Cadastro".center(30))
            print()
            nome = str(input("Nome: "))
            idade = int(input("Idade: "))
            cadastrar("arquivos.txt", nome, idade)
            linha()
        case 3:
            linha()
            print("Saindo do sistema... Volte sempre!")
            linha()

def arquivoExiste(nome):
    try:
        abrir = open(nome, "rt", encoding = "utf-8")
        abrir.close()
    except (FileNotFoundError):
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        abrir = open(nome, "wt+", encoding = "utf-8")
        abrir.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso.")

def lerArquivo(nome):
    try:
        abrir = open(nome, "rt", encoding = "utf-8")
    except:
        print("Erro ao ler o arquivo.")
    else:
        print(abrir.read())
    finally:
        abrir.close()

def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        abrir = open(arquivo, 'at')
    except:
        print("Houve um erro na abertura do arquivo.")
    else:
        try:
            abrir.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados.")
        else:
            print(f"Novo registro de {nome} adicionado com sucesso!")
            abrir.close()
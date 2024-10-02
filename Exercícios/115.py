from utilidades import módulo115
from time import sleep

sleep(0.5)
arquivo = "arquivos.txt"
if not módulo115.arquivoExiste(arquivo):
    módulo115.criarArquivo(arquivo)
módulo115.principal("Menu Principal")
sleep(0.5)
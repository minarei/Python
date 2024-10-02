import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print(f"\033[34mO site não está disponível no momento.\033[m")
else:
    print(f"\033[33mConsegui acessar o site.\033[m")
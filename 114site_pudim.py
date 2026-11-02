
import urllib.request
try:
    urllib.request.urlopen("http://www.pudim.com.br")
    print("Pudim está acessível!")
except:
    print("Pudim não está acessível!")
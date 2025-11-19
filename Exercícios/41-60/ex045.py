#0-1-1-2-3-4-8-13-21
from time import sleep
antecessor = 0
atual = 1
sucessor = antecessor + atual
N = int(input("Insira o valor de N (inteiro)\n---> "))
if(N == 0):
    print("Invalido.")
elif(N == 1):
    print(antecessor)
elif (N == 2):
    print(f"{antecessor} --> {atual}")
else:
    print(f"{antecessor} --> {atual}",end="")
    N -= 2

while (N >= 1):
    sucessor = antecessor + atual
    print(f"--> {sucessor}",end="")
    antecessor = atual
    atual = sucessor
    sleep(0.8)
    N -= 1
from time import sleep
#Contador que vai de 0 a 10
'''
contador = 1

while(contador != 11):
    print(contador)
    contador += 1
'''

'''
contador = 10
while(contador != -1):
    print(contador)
    contador -= 1
'''

#Criar um programa que some todos os numeros digiitados pelo ulizador.
#Quantos? Nao sei. So sei que se o utilizador digitar 0, e para parar
'''
soma = 0
numero = ''
while (numero != 0):
    numero = int(input("Insira um numero: "))
    soma += numero
print(soma)
'''
#Eu quero criar um programa que peçaos genero de uma pessoa
#Apenas aceita como resposta m ou f
#Se o utilizador digitar outra resposta ele vai ter de pedir novamente

'''
genero = ''
while (genero != "M" and genero != "F"):
    genero = input("Qual o teu genero? ").strip().upper()
print(f"Genero: {genero}")'''

#Quero criar um menu onde o utilizador pode escolher 3 opçoes
#Escrever "Olá", "tudo bem", sair do programa

'''from time import sleep
opçao = 0
print("MENU")
print("[ 1 ] -  Olá")
print("[ 2 ] -  Tudo bem")
print("[ 3 ] -  Sair")
print()
while(opçao != 1 and opçao != 2 and opçao != 3):
    opçao = int(input("Insira a opção:\n --> "))
    if (opçao !=1 and opçao != 2 and opçao != 3):
        print("Opçao Invalida!\n")
if (opçao == 1):
    print()
    print("Olá")
elif (opçao == 2):
    print()
    print("Tudo bem")
else:
    print()
    print("Saindo do programa", end=".")
    sleep(0.5)
    print(end=".")
    sleep(0.5)
    print(end=".")'''




'''while True:
    print("MENU")
    print("[ 1 ] -  Olá")
    print("[ 2 ] -  Tudo bem")
    print("[ 3 ] -  Sair")
    print()
    opçao = int(input("Opçao:\n -->"))
    if(opçao==1):
        print("Olá.")
    elif (opçao==2):
        print("Tudo bem")
    elif (opçao==3):
        print()
        print("Saindo do programa", end=".")
        sleep(0.5)
        print(end=".")
        sleep(0.5)
        print(end=".")
        break
    else:
        print("Opçao Invalida.")'''
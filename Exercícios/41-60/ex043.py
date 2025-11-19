from time import sleep
from datetime import datetime

date = datetime.today()
print(f"Bem vindo ao Calcula 2.0!\nData: {str(date)[:16]}")
print()
num1 = int(input("Insira o 1º Número: "))
num2 = int(input("Insira o 2º Número: "))
num3 = int(input("Insira o 3º Número: "))
opcao = ""
maior = 0
print()
while True:
    print("-_-_-_- MENU -_-_-_-")
    print("[ 1 ] SOMAR")
    print("[ 2 ] MULTIPLICAR")
    print("[ 3 ] MAIOR")
    print("[ 4 ] NOVOS NUMEROS")
    print("[ 5 ] SAIR DO PROGRAMA")
    print()
    sleep(0.2)
    opcao = int(input("Escolha uma opção!\n --> "))
    if (opcao == 1):
        print("Soma:")
        print(f"{num1} + {num2} + {num3} = {num1+num2+num3}")
        print()
    elif (opcao == 2):
        print("Multiplicação:")
        print(f"{num1} X {num2} X {num3} = {num1*num2*num3}")
        print()
    elif (opcao == 3):
        maior = num1
        if (num1 > num2 and num1 > num3):
            print(f" O maior numero inserido é o {maior}!")
        elif (num1 < num2 and num2 > num3):
            maior = num2
            print(f" O maior numero inserido é o {maior}!")
        else:
            maior = num3
            print(f" O maior numero inserido é o {maior}!")
    elif (opcao == 4):
        print()
        print(" ---NOVOS NUMEROS---")
        sleep(0.5)
        num1 = int(input("Insira o 1º Número: "))
        num2 = int(input("Insira o 2º Número: "))
        num3 = int(input("Insira o 3º Número: "))
        print()
    elif (opcao == 5):
        print("Saindo do programa", end=".")
        sleep(0.5)
        print(end=".")
        sleep(0.5)
        print(end=".")
        break

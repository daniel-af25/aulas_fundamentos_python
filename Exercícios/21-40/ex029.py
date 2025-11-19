from time import sleep
print("--- BEM VINDO AO PROGRAMA MAT25 ---\n")
sleep(0.5)
print("--- Calculadora ---")
print(" [ 1 ] - Tabuada")
print(" [ 2 ] - Calculadora")
print(" [ 3 ] - Numeros Pares")
print(" [ 4 ] - Sair\n")
sleep(0.5)
opcao = int(input("Escolha uma opção do programa!\n --> "))
if (opcao == 1):
    num_tabuada = int(input(f"Escolha um numero para a tabuada!\n --> "))
    print("CALCULANDO...")
    sleep(0.5)
    print(f"{num_tabuada} X 1 = {num_tabuada * 1}")
    print(f"{num_tabuada} X 2 = {num_tabuada * 2}")
    print(f"{num_tabuada} X 3 = {num_tabuada * 3}")
    print(f"{num_tabuada} X 4 = {num_tabuada * 4}")
    print(f"{num_tabuada} X 5 = {num_tabuada * 5}")
    print(f"{num_tabuada} X 6 = {num_tabuada * 6}")
    print(f"{num_tabuada} X 7 = {num_tabuada * 7}")
    print(f"{num_tabuada} X 8 = {num_tabuada * 8}")
    print(f"{num_tabuada} X 9 = {num_tabuada * 9}")
    print(f"{num_tabuada} X 10 = {num_tabuada * 10}")
    print()
elif (opcao == 2):
    calculo = input("Que operaçao deseja realizar? Possiveis: X , / , + , - . Insira o operando desejado.\n --> ")
    if (calculo == "X"):
        num1 = float(input("Escolha o primeiro numero para o calculo!\n --> "))
        num2 = float(input("Escolha o segundo numero para o calculo!\n --> "))
        print("CALCULANDO...")
        sleep(0.5)
        print(f" {num1} X {num2} = {num1*num2}")
    elif (calculo == "/"):
        num1 = float(input("Escolha o primeiro numero para o calculo!\n --> "))
        num2 = float(input("Escolha o segundo numero para o calculo!\n --> "))
        print("CALCULANDO...")
        sleep(0.5)
        print(f" {num1} / {num2} = {num1/num2}")
    elif (calculo == "+"):
        num1 = float(input("Escolha o primeiro numero para o calculo!\n --> "))
        num2 = float(input("Escolha o segundo numero para o calculo!\n --> "))
        print("CALCULANDO...")
        sleep(0.5)
        print(f" {num1} + {num2} = {num1+num2}")
    elif (calculo == "-"):
        num1 = float(input("Escolha o primeiro numero para o calculo!\n --> "))
        num2 = float(input("Escolha o segundo numero para o calculo!\n --> "))
        print("CALCULANDO...")
        sleep(0.5)
        print(f" {num1} - {num2} = {num1-num2}")
    else:
        print("ERRO!")
elif (opcao == 3):
    numpar = int(input("Escolha um numero!\n --> "))
    print("CALCULANDO...")
    sleep(0.5)
    if (numpar % 2 == 0):
        print("NUMERO PAR!")
    if (numpar % 2 != 0):
        print("NUMERO IMPAR!")
elif (opcao == 4):
    print("SAINDO...")
    sleep(1)
else:
    print("ERRO, POR FAVOR RESTARTE O PROGRAMA!")
print()
print("OBRIGADO POR O UTILIZAR O PROGRAMA MAT25!\n")
sleep(1)
print("FIM DO PROGRAMA.")





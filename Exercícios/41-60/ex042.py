from random import randint
from time import sleep
print("--- BEM VINDO AO JOGO ADIVINHA V2.0 ---\n")
num = randint(0, 10)
contador = 0
num_user = int(input("INSIRA UM NUMERO DE 0 A 10:\n --> "))
while True:
    if (num == num_user):
        contador += 1
        print(f"PARABENS! ACERTASTE, ERA O NUMERO {num}.")
        print(f"TENTIVAS: {contador}")
        break
    elif (num != num_user):
        print("ERRADO!")
        contador += 1
        if(num_user < num):
            print("+ ALTO")
            print()
            num_user = int(input("INSIRA UM NUMERO DE 0 A 10:\n --> "))
        elif (num_user > num):
            print("+ BAIXO")
            print()
            num_user = int(input("INSIRA UM NUMERO DE 0 A 10:\n --> "))
    else:
        print("ERRO.")
print()
print("FIM DO PROGRAMA", end=".")
sleep(0.5)
print(end=".")
sleep(0.5)
print(end=".")




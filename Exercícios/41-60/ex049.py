from time import sleep
from random import randint
from datetime import datetime

userplayn = 0
pcplay = 0
player_choice = ""
contador = 0
datestart = datetime.now()
dateend = ""
total = ""
print("Bem vindo ao Jogo PAR-IMPAR.")
print(f"Inicio: {str(datestart)[:16]}\n")
while True:
    pcplay = randint(0, 5)
    while True:
        userplayn = int(input("Insira um numero de 0-5!\n--> "))
        if (userplayn < 0 or userplayn > 5):
            print("Insira um valor válido!\n")
            continue  # vai logo para o proximo ciclo de while, bom para fazer validações.
        else:
            break
    while True:
        player_choice = input("[ PAR/IMPAR ]\n--> ").strip().upper()
        if(player_choice != "PAR" and player_choice != "IMPAR"):
            print("Digite PAR/IMPAR!\n")
        else:
            break
    print()
    if((userplayn + pcplay) % 2 == 0 ):
        if(player_choice == "PAR"):
            print(f"Ganhas-te! Era PAR, utilizas-te {userplayn} e o PC utilizou {pcplay}!")
            contador += 1
            print()
        elif(player_choice =="IMPAR"):
            print(f"Perdes-te! Era PAR, utilizas-te {userplayn} e o PC utilizou {pcplay}!")
            print(f"STREAK: {contador} Vitórias!")
            dateend = datetime.now()
            total = dateend - datestart
            total = int(total.total_seconds())
            total = total/60
            print(f"Aguentas-te {total:.2f} minutos sem perder!")
            break
    elif ((userplayn + pcplay) % 2 != 0):
        if (player_choice == "IMPAR"):
            print(f"Ganhas-te! Era IMPAR, utilizas-te {userplayn} e o PC utilizou {pcplay}!")
            contador += 1
            print()
        elif (player_choice == "PAR"):
            print(f"Perdes-te! Era IMPAR, utilizas-te {userplayn} e o PC utilizou {pcplay}!")
            print(f"STREAK: {contador} Vitórias!")
            dateend = datetime.now()
            total = dateend - datestart
            total = int(total.total_seconds())
            total = total / 60
            print(f"Aguentas-te {total:.2f} minutos sem perder!")
            break
from time import sleep
speed_user = int(input("Velocidade: "))
multab = 100
if (speed_user > 80):
    print("MULTADO!")
    print("A CALCULAR COIMA...\n")
    sleep(1)
    print(f"O VALOR DA COIMA É: {(speed_user-80)*7+multab}€!")
elif (speed_user <= 80):
    print("NAO MULTADO")
print()
print("FIM DO PROGRAMA...")
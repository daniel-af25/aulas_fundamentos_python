from time import sleep
limite_velocidade = 120
minimo_velocidade = 50
print("---- RADAR DE VELOCIDADE ---")
sleep(0.5)
velocidade = int(input("Velocidade ---> "))
print("A VERIFICAR VELOCIDADE.", end=".")
sleep(0.2)
print(end=".")
sleep(0.2)
print("\n")
if (velocidade > limite_velocidade):
    print(f"MULTADO!\n")
elif (velocidade < minimo_velocidade):
    print(f"ACELERA!\n")
else:
    print(f"BOA VIAGEM\n")
print(f"FIM DO PROGRAMA!")

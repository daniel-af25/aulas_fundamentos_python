from random import randint
print("--- BEM VINDO AO JOGO ADIVINHA V1.0 ---\n")
num = randint(0, 7)
num_user = int(input("INSIRA UM NUMERO DE 0 A 7:\n --> "))
if (num == num_user):
    print(f"PARABENS! ACERTASTE, ERA O NUMERO {num}.")
elif (num != num_user):
    print(f"PERDESTE! ERRASTE, ERA O NUMERO {num}.")
else:
    print("ERRO.")
print()
print("FIM DO PROGRAMA.")



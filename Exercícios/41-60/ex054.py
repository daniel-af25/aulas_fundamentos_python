tuple = (int(input("Digite o primeiro número: \n")),
         int(input("Digite o segundo número: \n")),
         int(input("Digite o terceiro número: \n")),
         int(input("Digite o quarto número: \n")))


c7 = 0
c5 = ""
for c in range(0, len(tuple)):
    if(tuple[c] == 7):
        c7 += 1
    if(tuple[c] == 5):
        c5 = c
        print(f"O numero 5 foi inserido na posiçao {c}.")
    if(tuple[c] % 2 == 0):
        print(f"{tuple[c]}, indice da tuple {c} é par.\n")
    else:
        print(f"{tuple[c]}, indice da tuple {c} não é par.\n")

print()
if(c7 != 0):
    print(f"O número 7 foi encontrado {c7} vez(es).")
else:
    print(f"O número 7 não foi encontrado nenhuma vez.")

if(c5 == ""):
    print(f"Nao foi encontrado o numero 5 em nenhuma das posiççoes.")
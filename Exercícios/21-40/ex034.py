contador = 0
for c in range (0,10):
    numero = int(input(f"Insira o {c+1}º número: "))
    if (numero % 2 == 0):
        contador = contador + 1
print()
print(f"Nos numero inseridos {contador} foram pares")
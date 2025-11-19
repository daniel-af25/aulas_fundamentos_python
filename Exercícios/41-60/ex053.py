from random import randint

tuple = (randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000))
maior = tuple[0]
menor = tuple[0]
print(f"{tuple}")
print(f"Crescente: {sorted(tuple)}")
print("Crescente: ", end="")
for valor in sorted(tuple):
    print(f"{valor} ", end="")
print()
for c in range(0, len(tuple)):
    if(maior < tuple[c]):
        maior = tuple[c]
    if(menor > tuple[c]):
        menor = tuple[c]
'''
Podemo utilizar as funçoes max() e min() para verificar o maior e menor de uma tuple
'''


print(f"Maior = {maior}\n")
print(f"Menor = {menor}\n")
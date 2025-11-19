#estante = input("Digite uma consola."), input("Digite outra consola.")

#Tupples são imutãveis ou seja apos definirmos a tupple nao conseguimos modificar os seus valores

nomes = ("Nadia", "Julia", "Alexandra", "Telmo",
        "Victor", "Rafael", "Daniel", "Leticia",
        "Roman", "Pedro", "Francisca", "Ines", 32, True, 3.14)

for c in range(0,len(nomes)):
    print(f"No indice {c} está o nome {nomes[c]}.")

contador = 0
for nome in nomes:
    print(f"No indice {contador} está o nome {nomes[contador]}.")
    contador += 1

print()

for indice, name in enumerate(nomes):
    if (indice % 2 == 0):
        print(f"{indice}º = {name}")


print(sorted(nomes))

print(type(nomes))
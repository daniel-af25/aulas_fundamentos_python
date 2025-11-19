'''from math import fsum

notas = list()

print(type(notas))

for c in range(0,5,1):
    nota = float(input(f"Insira a {c+1}ª nota: "))
    notas.append(nota)

media = fsum(notas) / len(notas)
print(media)


nomes = ["Nadia", "Julia", "Alexandra", "Telmo",
        "Victor", "Rafael", "Daniel", "Leticia",
        "Roman", "Pedro", "Francisca", "Ines"]

print(nomes)

nomes.append("Joao")

print(nomes)

for c in range(0,len(nomes)):
    print(f"{nomes[c]} ", end="")

nomes.insert(0,"Rita")

nomes.pop()

print(nomes)'''
'''
series = list()

for c in range(0,5,1):
    serie = input(f"Insere a {c+1}º série: ")
    series.append(serie)

print(series)
'''


series = list()
while True:
    print()
    print("[ 1 ] Inserir novo top 5")
    print("[ 2 ] Substituir série")
    print("[ 3 ] Mostrar novo top 5")
    print("[ 4 ] Sair")
    print()
    opcao = int(input("---> "))

    match (opcao):
        case 1:
             for c in range(0, 5, 1):
                serie = input(f"Insere a {c + 1}º série: ")
                series.append(serie)

        case 2:
               newserie = input(f"Insira a nova série: ")
               delserie = input(f"Digite a serie a remover: ")
               if (delserie not in series):
                    while True:
                        delserie = input(f"Digite a serie a remover: ")
                        if (delserie in series):
                            break
                        else:
                            continue
               ind_delserie = series.index(delserie)
               series[ind_delserie] = newserie
               print(f"Serie alterada com sucesso.\n")
        case 3:
            for c in range (0,len(series)):
                print(f"{c+1}º - {series[c]}")

        case 4:
             print(f"Leaving program", end=".")
             break
        case _:
            print(f"Opção Inválida.")
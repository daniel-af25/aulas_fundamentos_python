from time import sleep
maior_nota = 0
menor_nota = 21
soma = 0
media = 0
contador = 0
nota = 0
print("Para parar digite 0!\n")
while True:
    nota = float(input(f"{contador + 1}º nota: "))
    if (nota == 0):
        print(f"Total de notas inseridas: {contador} \n")
        print(f"Média: {soma/contador:.2f} \n")
        print(f"Maior Nota: {maior_nota} \n")
        print(f"Menor Nota: {menor_nota} \n")
        break
    elif (nota >= 0 and nota <= 20):
        contador += 1
        soma += nota
        if (maior_nota < nota):
            maior_nota = nota
        if (menor_nota > nota):
            menor_nota = nota
    else:
        print("Nota inválida inserida!\n")
        print("Saindo do programa", end=".")
        sleep(0.5)
        print(end=".")
        sleep(0.5)
        print(end=".")
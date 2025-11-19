'''
Melhora o exercicio 61.

A soma de todos os valores pares.
A soma dos valores da segunda coluna
O maior valor da terceira linha.

'''

numeros = list()
soma_pares = 0
soma_segunda_coluna = 0
maior_terceira_linha = 0



for linha in range(0,3):
    temp = list()
    for coluna in range (0,3):
        num = int(input(f"[{linha+1}][{coluna+1}]:\n--> "))
        if (num % 2 == 0):
            soma_pares += num
        if (coluna == 1):
            soma_segunda_coluna += num
        temp.append(num)
        if (linha == 2):
            if (coluna == 0):
                maior_terceira_linha = num
            else:
                if (maior_terceira_linha < num):
                    maior_terceira_linha = num
    numeros.append(temp)

print()

for lista in numeros:
    for valor in lista:
        print(valor, end="  ")
    print()


print(f"Soma Pares = {soma_pares}  ")
print(f"Soma Segunda Linha = {soma_segunda_coluna} ")
print(f"Maior Terceira Linha = {maior_terceira_linha} ")
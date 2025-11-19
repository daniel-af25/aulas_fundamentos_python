maior_idade = 0
menor_idade = 100000
for c in range(0,10):
    idade = int(input(f"Qual a idade da {c+1}ª Pessoa?\n"))
    while (idade < 0):
        idade = int(input(f"Qual a idade da {c + 1}ª Pessoa?\n"))
    if (c==0):
        menor_idade = idade
        maior_idade = idade
    if (idade > maior_idade):
        maior_idade = idade
    if (idade < menor_idade):
        menor_idade = idade
print()
print(f"{maior_idade} é a idade da pessoa mais velha.\n ")
print(f"{menor_idade} é a idade da pessoa mais nova.\n ")

from datetime import datetime

menor_idade = 0
maior_idade = 0
ano_atual = datetime.now().year
for c in range(0,7):
    data_nascimento = int(input(f"Qual a data de nascimento da {c+1}ª Pessoa?\n"))
    if (ano_atual - data_nascimento >= 18):
        maior_idade += 1
    else:
        menor_idade += 1
print()
print(f"{maior_idade} maiores de idade.\n ")
print(f"{menor_idade} menores de idade.\n ")

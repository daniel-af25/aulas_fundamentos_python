frase = input("Digite uma frase à escolha: ").lower()
print()
frase_corrigida = frase.replace(" ", "")
lenght = len(frase_corrigida)
contador = 0
for c in range (0,lenght // 2):
    if (frase_corrigida[c] == frase_corrigida[lenght-c-1]):
        contador += 1
if (contador == (lenght-1) / 2):
    print("A frase inserida é um palíndromo!")
else:
    print("A frase inserida não é um palíndromo!")



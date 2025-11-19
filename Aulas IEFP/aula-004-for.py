#range (inicio, fim, passo)
from time import sleep
#for c in range(0,5, 2): #Repetimos 5 vezes o que esta identado dentro do for e a variavel c vai incrementado

'''
soma = 0
for c in range(0,5):
    nota = float(input(f"Insira a {c+1}ª nota: "))
    soma += nota
    print(f"O valor da soma é {soma}")
    print()
media = soma / c+1
print(soma) '''

numero = 7
for c in range (0,10,1):
    print(f"{numero} x {c+1} = {numero * (c+1)}")
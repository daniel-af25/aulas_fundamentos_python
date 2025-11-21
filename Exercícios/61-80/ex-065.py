from random import randint
from time import sleep


qt_jogadores = int(input("Quantos jogadores irão jogar o jogo Max(6)?\n--> "))
while (qt_jogadores > 6 or qt_jogadores <=   0 ):
    print("Número de jogadores inválido.")
    qt_jogadores = int(input("Quantos jogadores irão jogar o jogo Max(6)?\n--> "))
ordem = list()
used_numbers = list()
for c in range(qt_jogadores):
    jogador = dict()
    jogador["Jogador"] = input(f"{c+1}º Jogador: ")
    num = randint(1,6)
    if (num in used_numbers):
        while(num in used_numbers):
            num = randint(1, 6)
    used_numbers.append(num)
    jogador["Jogada"] = num
    ordem.append(jogador.copy())

print("Calculando ordem",end=".")
sleep(0.5)
print(end=".")
sleep(0.5)
print(end=".")
print("\n")
for c in range(qt_jogadores):
    for j in range(0, qt_jogadores - c - 1):
        if ordem[j]["Jogada"] < ordem[j + 1]["Jogada"]:
            ordem[j + 1], ordem[j] = ordem[j], ordem[j + 1]
print(ordem)
print("\n")
for c in range(qt_jogadores):
    print(f"{c+1}ª Jogador = {ordem[c]["Jogador"]}")
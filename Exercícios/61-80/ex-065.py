from random import randint
from time import sleep

qt_jogadores = int(input("Quantos jogadores irão jogar o jogo Max(6)?\n--> "))
while (qt_jogadores > 6 or qt_jogadores < 0 ):
    print("Número de jogadores inválido.")
    qt_jogadores = int(input("Quantos jogadores irão jogar o jogo Max(6)?\n--> "))
Ordem = dict()
jogada = 0
for c in range(qt_jogadores):
    Ordem["Jogador"] = input(f"{c+1}º Jogador: ")
    jogada = randint(1,6)
    if (jogada in Ordem["Jogada"]):
        while(jogada in Ordem["jogadas"]):
            jogada = randint(1, 6)
    Ordem["Jogada"] = jogada

print("Calculando ordem",end=".")
sleep(0.5)
print(end=".")
sleep(0.5)
print(end=".")
print(Ordem)
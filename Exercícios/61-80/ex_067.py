from time import sleep
import os
opcao = 0
jogadores = list()
jogadores_ordenados = list()
contador = 0
while (opcao != 3):
    os.system("cls")
    print("=_=_=_=_=_= Arquivo Goal per Game =_=_=_=_=_=\n")
    print(f" [ 1 ] - Adicionar Jogador\n")
    print(f" [ 2 ] - Ver Ranking\n")
    print(f" [ 3 ] - Sair do Programa\n")
    opcao = int(input("Insira a sua opção:\n--> "))
    match (opcao):
        case 1:
            player = dict()
            os.system("cls")
            player["Nome"] = input("Nome Jogador: ")
            player["Jogos"] = int(input("Jogos Totais: "))
            while (player["Jogos"] < 0):
                player["Jogos"] = int(input("Jogos Totais: "))
            player["Golos_Totais"] = int(input("Golos Totais: "))
            while (player["Golos_Totais"] < 0):
                player["Golos_Totais"] = int(input("Golos Totais: "))
            print(".")
            golo_game = (player["Golos_Totais"] / player["Jogos"])
            player["Golo_Game"] = round(golo_game,2)
            jogadores.append(player.copy())
            contador += 1
        case 2:
            for c in range(len(jogadores)):
                print(f"{c+1}º Lugar: {jogadores[c]["Nome"]} - {jogadores[c]["Golo_Game"]}\n")
                sleep(3)

        case 3:
            print("Saindo do programa", end=".")
            sleep(0.5)
            print(end=".")
            sleep(0.5)
            print(end=".")
        case _:
            print("Escolhe uma opção válida!")

    for c in range (contador):
        for j in range (0, contador - c - 1):
            if jogadores[j]["Golo_Game"] < jogadores[j + 1]["Golo_Game"]:
                jogadores[j + 1], jogadores[j] = jogadores[j], jogadores[j + 1]

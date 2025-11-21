from time import sleep
import os
opcao = 0
pessoas = list()
contador = 0
media_idade = 0
mulheres = 0
homens_idade = 0
while (opcao != 6):
    os.system("cls")
    print("=_=_=_=_=_= Arquivo de Pessoas =_=_=_=_=_=\n")
    print(f" [ 1 ] - Adicionar Pessoa\n")
    print(f" [ 2 ] - Pessoas Registradas\n")
    print(f" [ 3 ] - Média de Idades do Grupo\n")
    print(f" [ 4 ] - Mulheres Registradas\n")
    print(f" [ 5 ] - Homens com idade acima da média\n")
    print(f" [ 6 ] - Sair do Programa\n")
    opcao = int(input("Insira a sua opção:\n--> "))
    match (opcao):
        case 1:
            pessoa = dict()
            pessoa["Nome"] = input("Digite o seu nome: ")
            pessoa["Sexo"] = input("Sexo (Masculino/Feminino): ")
            while(pessoa["Sexo"] != "Masculino" and pessoa["Sexo"] != "Feminino"):
                pessoa["Sexo"] = input("Sexo (Masculino/Feminino): ")
            pessoa["Idade"] = int(input("Digite a sua idade: "))
            while (pessoa["Idade"] < 0):
                pessoa["Idade"] = input("Idade:")
            pessoas.append(pessoa)
            contador += 1
        case 2:
            if (contador == 0):
                break
            print(f"{contador} Pessoas Registrada(s)")
        case 3:
            if (contador == 0):
                break
            for c in range(pessoas):
               media_idade += pessoas[c]["Idade"]
            media_idade = media_idade / contador
            print(f"Média Idade: {media_idade} anos.")
        case 4:
            if (contador == 0):
                break
            for c in range(pessoas):
                if (pessoas[c]["Sexo"] == "Feminino"):
                    mulheres += 1
            print(f"{mulheres} Mulheres Registradas.")
        case 5:
            if (contador == 0):
                break
            for c in range(pessoas):
                media_idade += pessoas[c]["Idade"]
            media_idade = media_idade / contador
            for c in range(pessoas):
                if(pessoas[c]["Sexo"] == "Masculino" and pessoas[c]["Idade"] > media_idade):
                   homens_idade += 1
            print(f"{homens_idade} Homens com idade acima da média.")
        case 6:
            print(f"Saindo do programa", end=".")
            sleep(0.5)
            print(end=".")
            sleep(0.5)
            print(end=".")
        case _:
            print("Escolhe uma opção válida!")


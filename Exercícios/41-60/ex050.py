idade = 0
total_maiores_25 = 0
homens_menores_17 = 0
total_mulheres = 0
total_menores_18 = 0

print("-_-_- RECOLHA ESTATÍSTICA -_-_-")
while True:
    while True:
            idade = int(input("\nQual a sua idade?\n--> "))
            if (0 <= idade <= 120):
                break
            else:
                print("ERRO: Por favor, insira uma idade válida (entre 0 e 120).")
    while True:
        genero = input("Qual o seu género (M/F)?\n--> ").strip().upper()
        if genero == "M" or genero == "F":
            break
        else:
            print("ERRO: Por favor, insira um género válido ('M' ou 'F').")

    if idade > 25:
        total_maiores_25 += 1
    if idade < 17 and genero == "M":
        homens_menores_17 += 1
    if genero == "F":
        total_mulheres += 1
    if idade < 18:
        total_menores_18 += 1

    while True:
        opcao = input("Deseja continuar? (S/N)\n--> ").strip().upper()
        if opcao == "S" or opcao == "N":
            break
        else:
            print("ERRO: Opção inválida! Por favor, responda com 'S' ou 'N'.")
    if opcao == "N":
        break
print("\n--- RESULTADOS DA ESTATÍSTICA ---")
print(f"{total_maiores_25} pessoas têm mais de 25 anos.")
print(f"{homens_menores_17} homens têm menos de 17 anos.")
print(f"{total_mulheres} pessoas são mulheres.")
print(f"{total_menores_18} pessoas são menores de idade (menos de 18 anos).")
print("---------------------------------")
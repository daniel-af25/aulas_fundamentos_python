aluno = dict()

aluno["Nome"] = input("Digite o seu nome: ")
aluno["Média"] = int(input("Digite a sua média: "))
aluno["Situação"] = "Aprovado" if (aluno["Média"] >= 9.5) else "Reprovado"

print(aluno)
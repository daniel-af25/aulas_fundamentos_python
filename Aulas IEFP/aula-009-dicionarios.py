'''aluno =  dict()
aluno["Nome"] = "Ricardo"
aluno["Média"] = 20
aluno["Situação"] = "Aprovado"
'''

turma = list()
qt_alunos = 2
aluno = dict()


for c in range(qt_alunos):
    aluno["Nome"] = input(f"Digite o nome do {c+1}º Aluno: ")
    aluno["Média"] = int(input("Digite a sua média: "))
    aluno["Situação"] = "Aprovado" if (aluno["Média"] >= 9.5) else "Reprovado"
    turma.append(aluno.copy())

print(turma[1])

'''if (aluno["Média"] > 9.5):
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"'''


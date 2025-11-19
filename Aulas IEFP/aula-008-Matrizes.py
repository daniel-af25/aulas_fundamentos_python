aluno1 = ["Telmo", 14]
aluno2 = ["Solinho", 17]
aluno3 = ["Pedro", 15]
aluno4 = ["Letícia", 15]


turma = list()


turma.append(aluno1[:])
turma.append(aluno2[:])
turma.append(aluno3[:])
turma.append(aluno4[:])

for aluno in turma:
    print(f"O/A aluno {aluno[0]} têm uma média = {aluno[1]} valores")
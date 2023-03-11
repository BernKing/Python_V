alunos = [{} for k in range(10)]
contador = 0

for i in range(10):
    print("Novo aluno")
    notas = []
    for k in range(4):
        notas.append(int(input("Notas:")))

    alunos[i].update({"notas:": notas})

    if sum(alunos[i]["notas:"]) / 4:
        contador += 1

print(contador)
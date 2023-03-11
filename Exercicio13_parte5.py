# ponto a não explicito logo numero de pessoas é escolhido pelo utilizador ao programar o programa

pessoas = [{} for k in range(2)]


def media_idades(vetor, num):
    contador_idades = 0
    for i in range(len(vetor)):
        contador_idades += vetor[i]["idade:"]

    if num == 1:
        return contador_idades / len(vetor)
    else:
        return print(contador_idades / len(vetor))


def acima_media_idades(vetor):
    media = media_idades(vetor, 1)
    pessoas_acima = []

    for i in range(len(vetor)):
        if vetor[i]["idade:"] > media:
            pessoas_acima.append(vetor[i])

    return print(pessoas_acima)


def lista_mulheres(vetor):
    mulheres = []

    for i in range(len(vetor)):
        if pessoas[i]["sexo:"] == "f":
            mulheres.append(vetor[i])

    return print(mulheres)


for i in range(2):
    print("Nova pessoa")

    pessoa = str(input("Nome:"))
    pessoas[i].update({"nome:": pessoa})

    sexo = str(input(("Sexo (m ou f):")))
    pessoas[i].update({"sexo:": sexo})

    idade = int(input("Idade:"))
    pessoas[i].update({"idade:": idade})

print("Numero pessoas:")
print(len(pessoas))
print("Media idades")
media_idades(pessoas, 0)
print("Acimda idade media:")
acima_media_idades(pessoas)
print("Mulheres:")
lista_mulheres(pessoas)

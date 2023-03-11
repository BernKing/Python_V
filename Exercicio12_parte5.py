# funcoes usadas ao extremo

def quantidade(vetor, num):
    if num == 0:
        return print(len(vetor))
    else:
        return len(vetor)


def mostrar(vetor):
    print(vetor)


def mostrar_inverso(vetor):
    vetor.reverse()
    return print(vetor)


def soma(vetor, num):
    if num == 0:
        return print(sum(vetor))
    else:
        return sum(vetor)


def media(vetor, num):
    if num == 0:
        return print(soma(vetor, 1) / quantidade(vetor, 1))
    else:
        return soma(vetor, 1) / quantidade(vetor, 1)


def valores_acima(vetor):
    mediaa = media(vetor, 1)
    somatorio = 0
    for i in range(quantidade(vetor, 1)):
        if vetor[i] > mediaa:
            somatorio += 1

    return print("Acima da media:", somatorio)


def valores_abaixo_dez(vetor):
    somatorio = 0
    for i in range(quantidade(vetor, 1)):
        if vetor[i] < 10:
            somatorio += 1

    return print("Abaixo de 10:", somatorio)


def valores_acima_dez(vetor):
    somatorio = 0
    for i in range(quantidade(vetor, 1)):
        if vetor[i] > 10:
            somatorio += 1

    return print("Acima de 10:", somatorio)


notas = []

r = 0

while r != -1:
    r = int(input("Nota:"))

    if r != -1:
        notas.append(r)

    else:
        break

quantidade(notas, 1)
mostrar(notas)
mostrar_inverso(notas)
soma(notas, 1)
media(notas, 1)
valores_acima(notas)
valores_acima_dez(notas)
valores_abaixo_dez(notas)

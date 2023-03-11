caracteres = []


def ver_consoantes(lista):
    consoantes = 0

    for char in lista:
        if char not in "aeiou":
            consoantes += 1

    return consoantes

for i in range(10):
    caracteres.append(input("Introduza letras"))

print(ver_consoantes(caracteres))

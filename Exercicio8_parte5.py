
lista = []
def soma(vetor):
    return sum(vetor)

def multiplicar(vetor):
    multi = 1
    for i in vetor:
        multi = multi * i
    return multi

def vetor():
    num = int(input("Numero:"))
    return num

for i in range(5):
    lista.append(vetor())

print("Soma:",soma(lista),"Multiplicar:",multiplicar(lista))




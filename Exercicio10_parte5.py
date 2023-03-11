def quadrado(x):
    return x^2

def membro():
    return int(input("Introduza um numero"))

vetor = []
for i in range(10):
    vetor.append(membro())
soma = 0
for i in range(len(vetor)):
    soma = soma + quadrado(vetor[i])

print(soma)
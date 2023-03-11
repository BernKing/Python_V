


vetor = []
pares = []
impares = []

for i in range(20):
    vetor.append(int(input("Numero:")))

for i in range(20):
    if vetor[i] % 2 == 0:
        pares.append(vetor[i])

    else:
        impares.append(vetor[i])


print(vetor)
print(pares)
print(impares)
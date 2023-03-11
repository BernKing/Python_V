def idade():
    return int(input("Introduza a idade"))

def altura():
    return int(input("Altura"))

alturas = []
idades = []

for i in range(5):
    alturas.append(altura())
    idades.append(idade())

alturas.reverse()
idades.reverse()
print(alturas)
print(idades)
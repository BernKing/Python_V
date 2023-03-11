def ler_lista():

    num = input("Numero:")
    return num


a = []
b = []
c = []
for i in range(5):
    numero = ler_lista()
    a.append(numero)
    c.append(numero)
print("nn")

for i in range(10):
    b.append(ler_lista())

c.extend(b)

print(a)
print(b)
print(c)
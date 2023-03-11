
respostas = []

respostas.append(str(input("Telefonou à vítima?")))
respostas.append(str(input("Esteve no local do crime?")))
respostas.append(str(input("Mora perto da vítima?")))
respostas.append(str(input("Devia dinheiro à vítima?")))
respostas.append(str(input("Já trabalhou com a vítima?")))

somatorio = 0

for resposta in respostas:
    if resposta in "sim":
        somatorio += 1


if somatorio < 2:
    print("Não explicitio")
elif somatorio == 2:
    print("Suspeito")
elif somatorio == 3 or somatorio == 4:
    print("Cumplice")
elif somatorio == 5:
    print("Assassino")
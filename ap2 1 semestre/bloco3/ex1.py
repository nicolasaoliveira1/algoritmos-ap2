# Controle de Combustível do Ônibus Espacial
cont = 0
combustivel = 1000
while cont < 10:
    consumo = int(input(f"Etapa {cont+1}: Quantos litros de combustível foram consumidos? "))
    combustivel = combustivel - consumo
    if consumo <= 100:
        print(f"Consumo seguro. Combustível restante: {combustivel} litros.")
    elif consumo > 100:
        print(f"Alto consumo! Combustível restante: {combustivel} litros.")
    if combustivel < 200:
        print("Missão abortada! Combustível insuficiente para continuar.")
        break
    cont += 1
    if cont == 10:
        print("Missão completa! Parabéns!")

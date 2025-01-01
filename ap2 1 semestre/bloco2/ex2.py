'''Faça um programa que receba a idade, o peso, a altura, a cor dos olhos (A-azul, P-preto,V-verde e C-castanho) e a cor dos cabelos (P-preto, C-castanho, L-louro e R-ruivo) de vinte pessoas,e que calcule e mostre:
a quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 quilos;
a média das idades das pessoas com altura inferior a 1,50 metro;
a percentagem de pessoas com olhos azuis e cabelos castanhos;
a quantidade de pessoas ruivas e que não possuem olhos verdes.
'''
cont = 0
cont_idade = 0
idades_baixos = 0
cinquenta = 0
olho_azul_cabelo_castanho = 0
ruivas_sem_olho_verde = 0
while cont < 20:
    idade = int(input(f"Digite a idade da {cont+1} pessoa: "))
    peso = float(input(f"Digite o peso da {cont+1} pessoa (Em kilogramas): "))
    altura = float(input(f"Digite a altura da {cont+1} pessoa (Em metros usando ponto): "))
    olho = input(f"Digite a cor do olho da {cont+1} pessoa (a - azul, p - preto, v - verde e c - castanho): ")
    cabelo = input(f"Digite a cor do cabelo da {cont+1} pessoa (p - preto, c - castanho, l - louro e r - ruivo): ")

    if idade > 50 and peso < 60:
        cinquenta += 1
    if altura < 1.50:
        cont_idade += 1
        idades_baixos += idade
    if olho == 'a' and cabelo == 'c':
        olho_azul_cabelo_castanho += 1
    if cabelo == 'r' and olho != 'v':
        ruivas_sem_olho_verde += 1
    cont += 1

if cont_idade > 0:
    media_idade = idades_baixos / cont_idade
else:
    media_idade = 0
porcentagem_azul_castanho = (olho_azul_cabelo_castanho / cont)*100

print(f"\nPessoas com idade superior a 50 com peso menor de 60 quilos: {cinquenta}")
print(f"Média da idade das pessoas com altura inferior a 1,50 metros: {media_idade:.2f}")
print(f"Porcentagem de pessoas de olho azul e cabelo castanho: {porcentagem_azul_castanho:.2f}%")
print(f"A quantidade de pessoas ruivas sem olho verde: {ruivas_sem_olho_verde}")

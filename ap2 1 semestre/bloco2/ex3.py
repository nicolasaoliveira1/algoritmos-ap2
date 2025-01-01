'''Faça um programa para cálculos de multas de um determinado número de veículos. O programa deve ler a velocidade de um veículo e ser encerrado quando uma velocidade negativa for digitada. 
Considere que a velocidade máxima da rodovia é de 80km/h e a margem de erro do é 5 km/h.
São 3 valores para a multa por excesso de velocidade e uma por velocidade baixa: 

Transitar em velocidade inferior à metade da velocidade máxima da rodovia.  R$130,16. Multa média. Obs: Não considerar margem de erro.
Até 20% acima do limite permitido: R$130,16. Multa média.
De 20% até 50% acima do limite permitido: R$195,23. Multa grave.
Acima de 50% do limite permitido: R$880,41. Multa gravíssima.

Ao término da leitura, informar:
Quantos veículos não tiveram multas.
Quantos veículos tiveram multa média.
Quantos veículos tiveram multa grave.
Quantos veículos tiveram multa gravíssima.
Imprimir o somatório total das multas.
Imprimir a média de velocidade da rodovia.
'''
limite = 85
cont = 0
sem_multa = 0
multa_media = 0
multa_grave = 0
multa_gravissima = 0
velocidades = 0
while cont < 10:
    velocidade = float(input(f"Qual a velocidade do {cont+1} carro: "))
    if velocidade < 0:
        print("A velocidade informada é inválida, tente novamente.")
        continue
    if velocidade <= limite and velocidade > 40:
        print(f"Velocidade {velocidade}km/h, não houve multa.")
        sem_multa +=1
    else:
        excesso = velocidade - limite
        percentual_excesso = (excesso/limite) * 100
        if velocidade < 40:
            print(f"Velocidade {velocidade}km/h, Multa Média R$130,16.")
            multa_media += 1
        elif percentual_excesso <= 20:
            print(f"Velocidade {velocidade}km/h, Multa Média R$130,16.")
            multa_media += 1
        elif percentual_excesso <= 50:
            print(f"Velocidade {velocidade}km/h, Multa Grave R$195,23.")
            multa_grave +=1
        else:
            print(f"Velocidade {velocidade}km/h, Multa Gravíssima R$880,41.")
            multa_gravissima +=1
    cont+=1
    velocidades += velocidade

mult1 = 130.16 * multa_media
mult2 = 195.23 * multa_grave
mult3 = 880.41 * multa_gravissima
somatorio = mult1 + mult2 + mult3
media_velocidades = velocidades / cont

print(f"\nVeículos que não levaram multa: {sem_multa}")
print(f"Veículos que tiveram multa média: {multa_media}")
print(f"Veículos que tiveram multa grave: {multa_grave}")
print(f"Veículos que tiveram multa gravíssima: {multa_gravissima}")
print(f"O somatório do total das multas é de: R${somatorio:.2f}")
print(f"A média de velocidade da rodovia é de: {media_velocidades}km/h")

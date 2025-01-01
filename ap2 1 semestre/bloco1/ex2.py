#Calculadora de multas de veículo
velocidade = float(input("Informe a velocidade do veículo em km/h: "))
if velocidade <= 87:
    print(f"Velocidade: {velocidade}km/h\nNão haverá multa.")
elif velocidade > 87 and velocidade <= 107:
    print(f"Velocidade {velocidade}km/h\nMulta média. R$130,16")
elif velocidade > 107 and velocidade <= 120:
    print(f"Velocidade {velocidade}km/h\nMulta grave. R$195,23")
else:
    print(f"Velocidade {velocidade}km/h\nMulta gravíssima. R$880,41")

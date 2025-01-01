#Cálculo de valores da empresa
faturamento = float(input("Digite o faturamento da empresa: "))
custos = float(input("Digite os custos da empresa: "))
pis = 0.0065
cofins = 0.03
valor_pis = pis * faturamento
valor_cofins = cofins * faturamento
impostos = valor_pis + valor_cofins
lucro = faturamento - (impostos + custos)
print(f"Faturamento: R${faturamento:.2f}")
print(f"Custos da empresa: R${custos:.2f}")
print(f"Valor de imposto PIS: R${valor_pis:.2f}")
print(f"Valor de COFINS: R${valor_cofins:.2f}")
print(f"Lucro da empresa: R${lucro:.2f}")
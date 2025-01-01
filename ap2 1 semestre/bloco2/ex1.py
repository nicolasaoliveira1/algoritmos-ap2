'''Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
A preço final para compra à vista tem desconto de 20%:
A quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60;
Os percentuais de acréscimo encontram-se na tabela.
'''
valor_carro = float(input("Digite o valor do carro: "))
pagamento = int(input("Escolha a forma de pagamento:\nParcelado: (1)\nÀ vista: (2)\n"))
parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
valor_parcelas = [0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24, 0.27, 0.3]
desconto = 0.2 * valor_carro
preco_final = valor_carro - desconto

if pagamento == 2:
    print("Pagamento à vista selecionado. Você terá um desconto de 20%")
    print(f"O preço final com o desconto será de R${preco_final:.2f}")

elif pagamento == 1:
    print(f"Opções de Parcelas: {parcelas}")
    parcela = int(input("Escolha a quantidade de parcelas: "))

    if parcela in parcelas:
        indice_parcela = parcelas.index(parcela)
        acrescimo = valor_parcelas[indice_parcela]
        preco_final = valor_carro * (1 + acrescimo)
        valor_parcela = preco_final / parcela
        print(f"Preço final do carro parcelado: R${preco_final:.2f}")
        print(f"Quantidade de parcelas: {parcela} parcelas de R${valor_parcela:.2f} cada")
    else:
        print("Quantidade de parcelas inválidas, tente novamente.")
else:
    print("Forma de pagamento inválida, tente novamente.")

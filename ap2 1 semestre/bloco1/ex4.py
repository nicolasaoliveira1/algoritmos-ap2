'''Faça um algoritmo para verificar se uma data é válida. Solicite que o usuário informe o dia, o mês e o ano. Lembre-se que os meses têm diferentes números de dias e que fevereiro tem 29 dias caso o ano seja bissexto. Informe na tela se o usuário digitou uma data válida.'''
print("Verificação de datas\n")
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    if mes == 2 and dia > 29:
        print(f"{dia}/{mes}/{ano} Data inválida\n{ano} é um ano bissexto. Fevereiro possui 29 dias.")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            print(f"{dia}/{mes}/{ano} Data inválida\nO mês 0{mes} possui 30 dias.")
        else:
            print("Ano bissexto")
            print(f"{dia}/{mes}/{ano} Data válida!")
    elif dia < 1 or dia > 31:
        print(f"{dia}/{mes}/{ano} Data inválida")
    elif mes < 1 or mes > 12:
        print(f"{dia}/{mes}/{ano} Data inválida")
    elif ano < 0:
        print(f"{dia}/{mes}/{ano} Data inválida")
    else:
        print("Ano bissexto")
        print(f"{dia}/{mes}/{ano} Data válida!")
else:
    if mes == 2 and dia > 28:
        print(f"{dia}/{mes}/{ano} Data inválida\nO mês de Fevereiro possui 28 dias (Em anos não bissextos).")
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            print(f"{dia}/{mes}/{ano} Data inválida\nO mês 0{mes} possui 30 dias.")
        else:
            print(f"{dia}/{mes}/{ano} Data válida!")
    elif dia < 1 or dia > 31:
        print(f"{dia}/{mes}/{ano} Data inválida")
    elif mes < 1 or mes > 12:
        print(f"{dia}/{mes}/{ano} Data inválida")
    elif ano < 0:
        print(f"{dia}/{mes}/{ano} Data inválida")
    else:
        print(f"{dia}/{mes}/{ano} Data válida!")

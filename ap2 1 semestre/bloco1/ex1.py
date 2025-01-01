#Horas perdidas de sono
print("Estudos dizem que para cada hora perdida de sono sua expectativa de vida diminui em 1.5 horas.")
horas = int(input("Quantas horas você dorme por dia: "))
meses = int(input("Há quantos meses você têm dormido desta forma: "))
dias = meses * 30
tempo = 8 - horas
horas_perdidas = (tempo * 1.5)*dias
dias_perdidos = horas_perdidas/24
if dias_perdidos < 0:
    print("\nVocê dorme mais que 8 horas por dia. Procure dormir entre 6-8 horas por dia.")
elif dias_perdidos == 0:
    print(f"\nVocê não diminuiu sua expectativa de vida nesses {meses} meses.")
    print("Seu sono está regulado. Parabéns!")
else:
    print(f"\nNesse período de {meses} meses você dormiu {tempo} horas a menos do ideal (8 horas por dia).")
    print(f"Logo, nesse período de {meses} meses, sua expectativa de vida diminuiu em {horas_perdidas:.0f} horas, ou seja, {dias_perdidos:.0f} dias.")
if horas < 4 and dias < 90:
    print("Procure melhorar sua qualidade de sono. Tente dormir entre 6-8 horas por dia.")
elif horas < 4 and dias > 90:
    print("Consequências do seu sono: Risco de problemas cardíacos e aumento do risco de acidentes.")
if (horas >= 4 and horas <= 6) and dias < 90:
    print("Procure melhorar sua qualidade de sono. Tente dormir entre 6-8 horas por dia.")
elif (horas >= 4 and horas <= 6) and (dias >= 180 and dias < 360):
    print("Consequências do seu sono: Diminuição da capacidade de memória e concentração.")
if (horas >= 6 and horas <= 8) and dias < 90:
    print("Procure melhorar sua qualidade de sono. Tente dormir entre 6-8 horas por dia.")
elif (horas >= 6 and horas <= 8) and dias >= 360:
    print("Consequências do seu sono: Menor risco de problemas de saúde e maior disposição física e mental.")
elif (horas > 8) and dias >= 360:
    print("Consequências do seu sono: Aumento do risco de doenças crônicas, como obesidade e diabetes.")

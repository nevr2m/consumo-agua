#Consumo Agua
# Tipo de imóvel
tipo_imovel = (input("Qual é o seu imóvel? (comercial, casa ou apartamento.): "))
# Consumo de água
consumo_agua = float(input("Consumo de água em m³(0-100): "))
#Regras
if tipo_imovel == "comercial": 
    print("Tarifa comercial aplicada - consulte o plano corporativo.")

elif tipo_imovel == "apartamento" and consumo_agua < 10:
    print("Consumo econômico - excelente controle de água!")

elif (tipo_imovel == "apartamento" or tipo_imovel == "casa") and consumo_agua <= 25:
     print("Consumo moderado - dentro do padrão residencial.")

else:
    print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
    
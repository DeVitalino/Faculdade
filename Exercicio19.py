#Joao paulo santos silva

litros = float(input("quantidade de combustivel usado para abastecer o carro (L): "))
km_por_litro = float(input("quantidade km o carro faz por litro:"))

distancia_maxima =  litros * km_por_litro

print(f"a distancia maxima percorrida que o carro podera chegar é: {distancia_maxima :.2f} km ")

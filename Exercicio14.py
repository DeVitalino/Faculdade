#Mateus Vitalino
combustivel = 2.50

print("SISTEMA TÁXI")


km_inicio = float(input("Digite a marcação do odômetro no INÍCIO do dia (Km): "))

km_fim = float(input("Digite a marcação do odômetro no FINAL do dia (Km): "))

litros_gastos = float(input("Digite a quantidade de litros de combustível gastos: "))

faturamento = float(input("Digite o valor total recebido dos passageiros (R$): "))

km_rodados = km_fim - km_inicio

media_consumo = km_rodados / litros_gastos

custo_combustivel = litros_gastos * combustivel
lucro_liquido = faturamento - custo_combustivel


print("\nRESUMO DO DIA")
print(f"Total de quilômetros rodados: {km_rodados:.1f} Km")

print(f"Média de consumo do veículo: {media_consumo:.2f} Km/L")

print(f"Custo com combustível: R$ {custo_combustivel:.2f}")

print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")


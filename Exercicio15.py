#Mateus Vitalino

print("SISTEMA DE VENDAS DA LOJA")

num_empregados = int(input("Número de empregados: "))

salario_minimo = float(input("Valor do salário-mínimo: "))

preco_custo_bike = float(input("Preço de custo da bike: "))

bikes_vendidas = int(input("Quantidade de bikes vendidas: "))

salario_fixo = 2 * salario_minimo

comissao_total = (preco_custo_bike * bikes_vendidas) * 0.15
comissao_cada = comissao_total / num_empregados
salario_final = salario_fixo + comissao_cada

preco_venda = preco_custo_bike * 1.50
faturamento = preco_venda * bikes_vendidas

custo_bikes = preco_custo_bike * bikes_vendidas
custo_RH = (salario_fixo * num_empregados) + comissao_total
lucro_loja = faturamento - (custo_bikes + custo_RH)

print("\nRESULTADOS")
print(f"Salario de cada um: R$ {salario_final:.2f}")
print(f"Lucro liquido da loja: R$ {lucro_loja:.2f}")

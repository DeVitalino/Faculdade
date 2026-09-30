#Mateus Vitalino

print("RENDA DO JOGO")

publico = int(input("Público total: "))

popular = (publico * 0.10) * 5
geral = (publico * 0.50) * 10
arquibancada = (publico * 0.30) * 20
cadeiras = (publico * 0.10) * 30

renda_total = popular + geral + arquibancada + cadeiras

print(f"Renda Total: R$ {renda_total:.2f}")

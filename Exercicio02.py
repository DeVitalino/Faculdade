#Mateus Vitalino
q = int(input("Digite a quantidade de notas: "))

resultado = []

for i in range(q):
    resultado.append(float(input("Digite a nota: ")))

media =  sum(resultado) / q

print("A média das notas é:", media)

#Mateus Vitalino
print("Bem-vindo ao Banco")

while True:

    taxa = 0.05
    opcao = input("\nMENU\n\n 1 - Depositar\n 2 - Sair\n\n Digite a opção desejada: ")


    if opcao == "1":

        q = float(input("Quanto você deseja guardar? "))
        rendimento = q * taxa

        total = q + rendimento

        print(f"Você vai depositar R${q:.2f}, e vai render por volta de R${rendimento:.2f} no mês.\n Totalizando R${total}")

    elif opcao == "2":
        print("Obrigado por usar o Banco! Até logo.")
        break
        
    else:
        print("Opção inválida! Tente novamente.")

#João Paulo
quantidade_livros = int(input("Digite a quantidade de livros comprados pelo cliente: "))

if quantidade_livros <= 10:
    preco_unitario = 12.00
else:
    preco_unitario = 8.00

valor_total = quantidade_livros * preco_unitario

print(f"O valor total da compra é: R$ {valor_total:.2f}")

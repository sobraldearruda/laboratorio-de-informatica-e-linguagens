# Exercício 15 - Aluguel de Carros

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
valor = (dias * 60) + (km * 0.15)
print(f"O total a pagar é de R${valor:.2f}.")

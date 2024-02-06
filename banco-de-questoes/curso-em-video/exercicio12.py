# Exercício 12 - Calculando Descontos

num = float(input("Qual o preço do produto? R$"))
desconto = float(input("Quantos porcento de desconto? "))
porcentagem = num * desconto / 100
print(f"O produto que custava {num:.2f}, 
      na promoção com desconto de {desconto:.2f}% vai custar {num-porcentagem:.2f}.")

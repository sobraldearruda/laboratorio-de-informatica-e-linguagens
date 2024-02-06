# Exercício 70 - Estatísticas em Produtos

total = mais = menor = cont = 0
menos = ""
print("-" * 30)
print("LOJA SUPER BARATÃO")
print("-" * 30)
while True:
  nome = input("Nome do produto: ")
  preco = float(input("Preço: R$"))
  total += preco
  cont += 1
  if preco > 1000:
    mais += 1
  if cont == 1 or preco < menor:
    menor = preco
    menos = nome
  continuar = input("Quer continuar? [S/N]").lower()
  if continuar == "n":
    print("-" * 30)
    print("FIM DO PROGRAMA")
    print("-" * 30)
    break
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {mais} produto(s) custando mais de R$1000.00")
print(f"O produto mais barato foi {menos} que custa R${menor:.2f}")

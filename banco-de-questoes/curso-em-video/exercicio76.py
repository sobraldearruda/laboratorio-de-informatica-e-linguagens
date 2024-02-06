# Exercício 76 - Lista de Preços com Tupla

print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)
lista = ("Lápis", 1.75,
         "Borracha", 2.00,
         "Caderno", 15.90,
         "Estojo", 25.00,
         "Transferidos", 4.20,
         "Compasso", 9.99,
         "Mochila", 120.32,
         "Canetas", 22.30,
         "Livro", 34.90)
for l in range(0, len(lista)):
  if l % 2 == 0:
    print(f"{lista[l]:.<30}", end="")
  else:
    print(f"R${lista[l]:>7.2f}")
print("-" * 40)

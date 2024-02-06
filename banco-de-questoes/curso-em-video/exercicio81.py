# Exercício 81 - Extraindo Dados de uma Lista

lista = []
cont = 0
while True:
  lista.append(int(input("Digite um valor: ")))
  cont += 1
  continuar = input("Quer continuar? [S/N] ").lower()
  if continuar == "n":
    break
print("=" * 70)
print(f"Você digitou {cont} elementos.")
lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}.")
if 5 in lista:
  print("O valor 5 faz parte da lista.")
else:
  print("O valor 5 não foi encontrado na lista.")

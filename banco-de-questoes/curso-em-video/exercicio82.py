# Exercício 82 - Dividindo Valores em Várias Listas

lista = []
pares = []
impares = []
while True:
  num = int(input("Digite um número: "))
  lista.append(num)
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)
  cont = input("Quer continuar? [S/N] ").lower()
  if cont == "n":
    break
print("=-" * 30)
print(f"A lista completa é {lista}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")

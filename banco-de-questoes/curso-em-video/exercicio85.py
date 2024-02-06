# Exercício 85 - Lista com Pares e Ímpares

lista = [[], []]
for l in range(1, 8):
  num = int(input(f"Digite o {l}º valor: "))
  if num % 2 == 0:
    lista[0].append(num)
  else:
    lista[1].append(num)
print("-=" * 40)
print(f"Os valores pares digitados foram: {sorted(lista[0])}.")
print(f"Os valores ímpares digitados foram: {sorted(lista[1])}.")

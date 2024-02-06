# Exercício 78 - Maior e Menor Valores na Lista

valores = []
maior = menor = 0
for v in range(0, 5):
  valores.append(int(input(f"Digite um valor para a Posição {v}: ")))
  if v == 0:
    maior = menor = valores[v]
  else:
    if valores[v] > maior:
      maior = valores[v]
    if valores[v] < menor:
      menor = valores[v]
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for p, val in enumerate(valores):
  if val == maior:
    print(f"{p}... ", end="")
print(f"\nO menor valor digitado foi {menor} nas posições ", end="")
for p, val in enumerate(valores):
  if val == menor:
    print(f"{p}... ", end="")

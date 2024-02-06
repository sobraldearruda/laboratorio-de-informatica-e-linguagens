# Exercício 48 - Soma Ímpares Múltiplos de 3

soma = 0
contador = 0
for impares in range(1, 501, 2):
  if impares % 3 == 0:
    soma += 1
    contador += impares
    print(impares, end=" ")
print(f"A soma de todos os {soma} valores é {contador}")

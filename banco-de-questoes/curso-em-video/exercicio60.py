# Exercício 60 - Cálculo do Fatorial

import math

num = int(input("Digite um número para calcular seu fatorial: "))
fatorial = math.factorial(num)
cont = num
while cont > 0:
  print(f"{cont}", end=" ")
  print(f"x" if cont > 1 else "=", end=" ")
  cont -= 1
print(f"{fatorial}")

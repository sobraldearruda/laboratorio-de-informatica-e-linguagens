# Exercício 52 - Números primos

cont = 0
num = int(input("Digite um número: "))
for n in range(1, num+1):
  print(n, end=" ")
  if num % n == 0:
    cont += 1
print(f"\nO número {num} foi divisível {cont} vezes.")
if cont > 2:
  print("E por isso não é primo.")
else:
  print("E por isso é primo.")

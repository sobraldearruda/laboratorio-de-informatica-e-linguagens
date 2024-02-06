# Exercício 50 - Soma dos pares

contador = 0
soma = 0
for n in range(0, 6):
  num = int(input("Digite um número:"))
  contador += 1
  if num % 2 == 0:
    soma += num
print(f"Você informou {contador} números e a soma foi {soma}.")

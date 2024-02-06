# Exercício 65 - Maior e Menor Valores

continuar = "s"
cont = 0
soma = []
maior = 0
menor = 0
while continuar != "n":
  num = int(input("Digite um número: "))
  continuar = input("Quer continuar? [S/N] ").strip().lower()
  cont += 1
  soma.append(num)
  maior = num
  menor = num
for s in soma:
  if maior < s:
    maior = s
  if menor > s:
    menor = s
print(f"Você digitou {cont} números e a média foi {(sum(soma) / cont):.2f}.")
print(f"O maior valor foi {maior} e o menor foi {menor}.")

# Exercício 75 - Análise de Dados em uma Tupla

num = (int(input("Digite um número: ")), int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
print(f"Você digitou os valores {num}")
if 9 in num:
  print(f"O valor 9 apareceu {num.count(9)} vezes")
else:
  print("O valor 9 não foi digitado em nenhuma posição")
if 3 in num:
  print(f"O valor 3 apareceu na {num.index(3)+1}ª posição")
else:
  print(f"O valor 3 não foi digitado em nenhuma posição")
print(f"Os valores pares digitados foram ", end="")
for n in num:
  if n % 2 == 0:
    print(f"{n} ", end="")

# Exercício 79 - Valores Únicos em uma Lista

num = []
while True:
  numero = int(input("Digite um valor: "))
  if numero not in num:
    num.append(numero)
    print("Valor adicionado com sucesso...")
  else:
    print("Valor duplicado! Não vou adicionar...")
  continuar = input("Quer continuar? [S/N] ").lower()
  if continuar == "n":
    break
print("=" * 30)
print(f"Você digitou os valores {sorted(num)}")

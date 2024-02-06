# Exercício 61 - Progressão Aritmética 2.0

print("=" * 20)
print("GERADOR DE PA")
print("=" * 20)
termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
cont = 1
while cont <= 10:
  print(f"{termo}", end=" -> ")
  termo += razao
  cont += 1
print("FIM!")

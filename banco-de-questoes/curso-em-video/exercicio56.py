# Exercício 56 - Analisador Completo

media_idade = 0
mais_velho1 = 0
mais_velho2 = ""
mulheres = 0
for p in range(1, 5):
  print("=" * 10, f"{p}ª PESSOA", "=" * 10)
  nome = input("Nome: ").strip()
  idade = int(input("Idade: "))
  media_idade += idade
  sexo = input("Sexo: [M/F] ").strip().lower()
  if sexo == "m":
    mais_velho1 = idade
    mais_velho2 = nome
    if idade > mais_velho1:
      mais_velho1 = idade
      mais_velho2 = nome
  else:
    if idade < 20:
      mulheres += 1
print(f"A média de idade do grupo é de {(media_idade / 4):.1f}.")
print(f"O homem mais velho tem {mais_velho1} anos e se chama {mais_velho2}.")
print(f"Ao todo são {mulheres} mulheres com menos de 20 anos.")

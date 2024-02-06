# Exercício 69 - Análise de Dados do Grupo

maior = menor = homens = 0
while True:
  print("-" * 20)
  print("CADASTRE UMA PESSOA")
  print("-" * 20)
  idade = int(input("Idade: "))
  sexo = input("Sexo: [M/F] ").lower()
  print("-" * 20)
  continuar = input("Quer continuar? [S/N] ").lower()
  if idade >= 18:
    maior += 1
  if sexo == "m":
    homens += 1
  if sexo == "f" and idade < 20:
    menor += 1
  if continuar == "n":
    break
print(f"Total de pessoas com mais de 18 anos: {maior}")
print(f"Ao todo temos {homens} homens cadastrados")
print(f"E temos {menor} mulheres com menos de 20 anos")

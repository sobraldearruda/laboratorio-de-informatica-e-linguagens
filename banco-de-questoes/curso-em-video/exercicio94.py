# Exercicio 94 - Unindo Dicionários e Listas

pessoa = {}
lista = []
soma = 0
while True:
  pessoa["nome"] = input("Nome: ")
  while True:
    pessoa["sexo"] = input("Sexo: [M/F] ").lower()[0]
    if pessoa["sexo"] in "mf":
      break
    print("ERRO! Digite apenas M ou F.")
  pessoa["idade"] = int(input("Idade: "))
  soma += pessoa["idade"]
  lista.append(pessoa.copy())
  while True:
    continuar = input("Quer continuar? [S/N] ").lower()[0]
    if continuar in "sn":
      break
    print("ERRO! Digite apenas S ou N.")
  if continuar == "n":
    break
print("-=" * 20)
print(f"A) Ao todo temos {len(lista)} pessoas cadastradas.")
media = soma / len(lista)
print(f"B) A média de idade é de {media:.2f} anos.")
print(f"C) As mulheres cadastradas foram ", end="")
for p in lista:
  if p["sexo"] == "f":
    print(f"{p['nome']} ", end="")
print()
print(f"D) Lista das pessoas que estão acima da média: ")
for p in lista:
  if p["idade"] > media:
    for k, v in p.items():
      print(f"{k} = {v}; ", end="")
    print()
print("<< ENCERRADO >>")

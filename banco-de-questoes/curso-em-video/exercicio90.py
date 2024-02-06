# Exercício 90 - Dicionário em Python

aluno = dict()
aluno["nome"] = input("Nome: ")
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))
print("=-" * 20)
print(f"O nome é igual a {aluno['nome']}.")
print("=-" * 20)
print(f"A média é igual a {aluno['media']}.")
print("=-" * 20)
if aluno["media"] >= 7:
  aluno["situacao"] = "Aprovado/a"
elif aluno["media"] >= 5:
  aluno["situacao"] = "Recuperação"
else:
  aluno["situacao"] = "Reprovado"
print(f"A situação é igual a {aluno['situacao']}.")
print("=-" * 20)

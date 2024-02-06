# Exercício 92 - Cadastro de Trabalhador em Python

import datetime

dic = dict()
dic["nome"] = input("Nome: ")
nascimento = int(input("Nascimento: "))
dic["idade"] = datetime.datetime.now().year - nascimento
dic["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
if dic["ctps"] != 0:
  dic["contratação"] = int(input("Ano de Contratação: "))
  dic["salário"] = int(input("Salário: R$ "))
  dic["aposentadoria"] = dic["idade"] + ((dic["contratação"] + 35) - datetime.datetime.now().year)
print("-=" * 20)
for k, v in dic.items():
  print(f"- {k} tem o valor {v}.")

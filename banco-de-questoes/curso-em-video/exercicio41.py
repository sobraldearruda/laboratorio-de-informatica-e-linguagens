# Exercício 41 - Classificando Atletas

import datetime

nascimento = int(input("Nascimento: "))
data = datetime.date.today().year
idade = data - nascimento
print(f"O atleta tem {idade} anos.")
if idade <= 9:
  print("Classificação: MIRIM")
elif idade > 9 and idade <= 14:
  print("Classificação: INFANTIL")
elif idade > 14 and idade <= 19:
  print("Classificação: JUNIOR")
elif idade > 19 and idade <= 25:
  print("Classificação: SENIOR")
else:
  print("Classificação: MASTER")

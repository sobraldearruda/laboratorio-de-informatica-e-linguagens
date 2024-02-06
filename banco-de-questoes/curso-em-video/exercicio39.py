# Exercício 39 - Alistamento Militar

import datetime

nascimento = int(input("Ano de nascimento: "))
ano = datetime.date.today().year
idade = ano - nascimento
print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano}.")
if idade < 18:
  print(f"Ainda faltam {18 - idade} anos para o alistamento.")
  print(f"O alistamento será em {(18 - idade) + ano}.")
elif idade > 18:
  print(f"Você já deveria ter se alistado há {idade - 18} anos.")
  print(f"Seu alistamento foi em {nascimento + 18}.")
else:
  print("Você tem que se alistar IMEDIATAMENTE!")

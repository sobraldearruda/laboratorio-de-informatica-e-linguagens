# Exercício 54 - Grupo da Maioridade

import datetime

ano = datetime.date.today().year
maior = 0
menor = 0
for n in range(1, 8):
  num = int(input(f"Em que ano a {n}ª pessoa nasceu? "))
  idade = ano - num
  if idade >= 21:
    maior += 1
  else:
    menor += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade.")
print(f"E também tivemos {menor} pessoas menores de idade.")

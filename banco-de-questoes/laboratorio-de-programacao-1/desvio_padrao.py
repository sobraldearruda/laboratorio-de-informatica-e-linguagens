## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Desvio padrão

import math

sequence1 = input().split()
sequence2 = input().split()
count1 = 0
for s in sequence1:
  count1 += float(s)
average1 = count1 / len(sequence1)
number1 = 0
for s in sequence1:
  number1 = number1 + ((float(s) - average1) ** 2)
deviation1 = math.sqrt(number1 / (len(sequence1) - 1))
count2 = 0
for s in sequence2:
  count2 += float(s)
average2 = count2 / len(sequence2)
number2 = 0
for s in sequence2:
  number2 = number2 + ((float(s) - average2) ** 2)
deviation2 = math.sqrt(number2 / (len(sequence2) - 1))
if deviation1 > deviation2:
  print(f"A sequência 1 possui o maior desvio padrão ({deviation1:.2f}).")
elif deviation2 > deviation1:
  print(f"A sequência 2 possui o maior desvio padrão ({deviation2:.2f}).")
else:
  print(f"As sequências possuem o mesmo desvio padrão ({deviation1:.2f}).")

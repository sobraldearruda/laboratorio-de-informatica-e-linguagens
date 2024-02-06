# Exercício 91 - Jogo de Dados em Python

import random
import operator

dic = {"um": random.randint(1, 6),
       "dois": random.randint(1, 6),
       "tres": random.randint(1, 6),
       "quatro": random.randint(1, 6)}
for k, v in dic.items():
  print(f"O jogador {k} tirou {v} no dado.")
print("-=" * 20)
print("== RANKING DOS JOGADORES ==")
ranking = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
  print(f"{i+1}º lugar: jogador {v[0]} com {v[1]}.")

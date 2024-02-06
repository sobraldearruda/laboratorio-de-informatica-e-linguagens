# Exercício 28 - Jogo da Adivinhação

import random
import time

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente advinhar...")
print("-=-" * 20)
num = int(input("Em que número eu pensei? "))
computador = random.randint(0,5)
print("PROCESSANDO...")
time.sleep(5)
if num == computador:
  print("PARABÉNS! Você conseguiu me vencer!")
else:
  print(f"GANHEI! Eu pensei no número {computador} e não no {num}!")

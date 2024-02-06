# Exercício 58 - Jogo da Adivinhação 2.0

import random
import time

print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)
computador = random.randint(0,10)
print("PROCESSANDO...")
time.sleep(5)
cont = 0
acertou = False
while not acertou:
  jogador = int(input("Qual é seu palpite? "))
  cont += 1
  if jogador == computador:
    acertou = True
  else:
    if jogador < computador:
      print("Mais... Tente novamente.")
    elif jogador > computador:
      print("Menos... Tente novamente.")
print(f"Acertou com {cont} tentativas. Parabéns!")

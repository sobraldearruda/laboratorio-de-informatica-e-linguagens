# Exercício 68 - Jogo do Par ou Ímpar

import random

total = 0
venceu = 0
while True:
  print("=-" * 20)
  print("VAMOS JOGAR PAR OU ÍMPAR")
  print("=-" * 20)
  num = int(input("Diga um valor: "))
  parimpar = input("Par ou Ímpar? [P/I] ").lower()
  comp = random.randint(0,11)
  jogador = 0
  computador = 0
  jogador += num
  computador += comp
  total = jogador + computador
  if total % 2 == 0:
    if parimpar == "p":
      print("-" * 20)
      print(f"Você jogou {num} e o computador {comp}. Total de {total} DEU PAR.")
      print("-" * 20)
      print("Você venceu!")
      print("Vamos jogar novamente...")
      venceu += 1
    else:
      print(f"Você jogou {num} e o computador {comp}. Total de {total} DEU ÍMPAR.")
      print("Você perdeu!")
      print("=-" * 20)
      print(f"GAME OVER! Você venceu {venceu} vezes.")
      break
  else:
    if parimpar == "i":
      print("-" * 20)
      print(f"Você jogou {num} e o computador {comp}. Total de {total} DEU ÍMPAR.")
      print("-" * 20)
      print("Você venceu!")
      print("Vamos jogar novamente...")
      venceu += 1
    else:
      print(f"Você jogou {num} e o computador {comp}. Total de {total} DEU PAR.")
      print("Você perdeu!")
      print("=-" * 20)
      print(f"GAME OVER! Você venceu {venceu} vezes.")
      break

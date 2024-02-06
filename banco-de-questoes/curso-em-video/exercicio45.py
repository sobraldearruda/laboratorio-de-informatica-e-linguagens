# Exercício 45 - Pedra, Papel e Tesoura

import random

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input("Qual é a sua jogada? "))
itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(0,2)
print(f"Computador jogou {itens[computador]}.")
print(f"Jogador jogou {itens[jogada]}")
if computador == 0:
  if jogada == 0:
    print("EMPATE")
  elif jogada == 1:
    print("JOGADOR VENCE")
  elif jogada == 2:
    print("COMPUTADOR VENCE")
  else:
    print("JOGADA INVÁLIDA")
elif computador == 1:
  if jogada == 0:
    print("COMPUTADOR VENCE")
  elif jogada == 1:
    print("EMPATE")
  elif jogada == 2:
    print("JOGADOR VENCE")
  else:
    print("JOGADA INVÁLIDA")
elif computador == 2:
  if jogada == 0:
    print("JOGADOR VENCE")
  elif jogada == 1:
    print("COMPUTADOR VENCE")
  elif jogada == 2:
    print("EMPATE")
  else:
    print("JOGADA INVÁLIDA")

# Exercício 88 - Palpites para a Mega Sena

from random import randint
from time import sleep

lista = list()
jogos = list()
print("-" * 50)
print("JOGA NA MEGA SENA".center(50))
print("-" * 50)
quant = int(input("Quantos jogos você quer que eu sorteie? ".center(50)))
tot = 1
while tot <= quant:
  cont = 0
  while True:
    num = randint(0, 60)
    if num not in lista:
      lista.append(num)
      cont += 1
    if cont >= 6:
      break
  lista.sort()
  jogos.append(lista[:])
  lista.clear()
  tot += 1
print("-" * 50)
print(f"SORTEANDO {quant} JOGOS".center(50))
print("-" * 50)
for i, l in enumerate(jogos):
  print(f"Jogo {i+1}: {l}".center(50))
  sleep(1)
print("-" * 50)
print("< BOA SORTE >".center(50))
print("-" * 50)

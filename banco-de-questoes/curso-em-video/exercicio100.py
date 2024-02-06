# Exercício 100 - Funções para Sortear e Somar

import random

def sorteia(lista):

  """Sorteia valores de uma lista."""

  print("Sorteando 5 valores na lista: ", end="")
  for cont in range(0, 5):
    n = random.randint(1, 10)
    lista.append(n)
    print(f"{n} ", end="", flush=True)
  print("PRONTO!")

def somaPar(lista):

  """Soma valores pares de uma lista."""

  soma = 0
  for valor in lista:
    if valor % 2 == 0:
      soma += valor
  print(f"Somando os valores pares de {lista}, temos {soma}.")


numeros = list()
sorteia(numeros)
somaPar(numeros)

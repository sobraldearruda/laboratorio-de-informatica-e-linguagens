# Exercício 102 - Função para Fatorial

def fatorial(n, show=False):

  """Calcula o fatorial de um número."""

  f = 1
  for c in range(n, 0, -1):
    if show:
      print(c, end="")
      if c > 1:
        print(" x ", end="")
      else:
        print(" = ", end="")
    f *= c
  return f


print(fatorial(5, show=True))

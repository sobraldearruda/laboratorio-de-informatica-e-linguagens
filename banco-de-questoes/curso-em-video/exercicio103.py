# Exercício 103 - Ficha do Jogador

def ficha(jog="<desconhecido>", gol=0):

  """Produz uma ficha para um jogador de futebol."""

  print(f"O jogador {jog} fez {gol} gol(s) no campeonato.")


n = input("Nome do Jogador: ")
g = input("Número de gols: ")
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n.strip() == "":
  ficha(gol=g)
else:
  ficha(n, g)

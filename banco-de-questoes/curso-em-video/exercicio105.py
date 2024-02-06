# Exercício 105 - Analisando e Gerando Dicionários

def notas(*n, sit=False):

  """Analisa notas e situação de alunos."""

  r = dict()
  r["total"] = len(n)
  r["maior"] = max(n)
  r["menor"] = min(n)
  r["media"] = sum(n)/len(n)
  if sit:
    if r["media"] >= 7:
      r["situação"] = "BOA"
    elif r["media"] >= 5:
      r["situação"] = "RAZOÁVEL"
    else:
      r["situação"] = "RUIM"
  return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)

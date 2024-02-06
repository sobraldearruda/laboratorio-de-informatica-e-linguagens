# Exercício 101 - Função para Votação

def voto(ano):

  """Valida votação por idade."""

  import datetime
  atual = datetime.date.today().year
  idade = atual - ano
  saida = ""
  if idade < 16:
    saida = f"Com {idade} anos: NÃO VOTA."
  elif 16 <= idade < 18 or idade > 65:
    saida = f"Com {idade} anos: VOTO OPCIONAL."
  else:
    saida = f"Com {idade} anos: VOTO OBRIGRATÓRIO."
  return saida


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))

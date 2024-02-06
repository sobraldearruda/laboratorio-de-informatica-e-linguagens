# Exercício 104 - Validando Entrada de Dados em Python

def leiaInt(msg):

  """Valida apenas entradas de dados em números inteiros."""

  ok = False
  valor = 0
  while True:
    n = input(msg)
    if n.isnumeric():
      valor = int(n)
      ok = True
    else:
      print("ERRO! Digite um número inteiro válido.")
    if ok:
      break
  return valor


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")

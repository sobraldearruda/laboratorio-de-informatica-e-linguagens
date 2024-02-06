# Exercício 106 - Interactive Helping System in Python

def ajuda(com):

  """Manual de ajuda de Python."""

  help(com)

def titulo(msg, cor=0):

  """Formata uma mensagem."""

  tam = len(msg) + 4
  print("~" * tam)
  print(f"  {msg}")
  print("~" * tam)


comando = ""
while True:
  titulo("SISTEMA DE AJUDA PYTHON")
  comando = input("Função ou Biblioteca Python > ")
  if comando.lower() == "fim":
    break
  else:
    ajuda(comando)
titulo("ATÉ LOGO!")

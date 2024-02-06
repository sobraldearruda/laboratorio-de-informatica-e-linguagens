# Exercício 97 - Um Print Especial

def escreva(msg):

  """Formata a saída de dados de acordo com o tamanho da mensagem."""

  tam = len(msg) + 4
  print("~" * tam)
  print(f"  {msg}")
  print("~" * tam)


escreva("Rafael")
escreva("Linguagem Python")
escreva("Programação")

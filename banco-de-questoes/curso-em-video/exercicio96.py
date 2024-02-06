# Exercício 96 - Função que calcula área

def calcula_area(largura, comprimento):

  """Calcula a área de um terreno"""

  area = largura * comprimento
  return area

print("Controle de terrenos")
print("-" * 20)
largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area = calcula_area(largura, comprimento)
print(f"A área de um terreno {largura}x{comprimento} é de {area}m².")

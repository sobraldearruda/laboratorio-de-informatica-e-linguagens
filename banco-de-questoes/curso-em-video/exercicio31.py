# Exercício 31 - Custo da Viagem

distancia = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia:.1f}Km.")
if distancia <= 200:
  passagem1 = distancia * 0.50
  print(f"E o preço de sua passagem será de R${passagem1:.2f}")
else:
  passagem2 = distancia * 0.45
  print(f"E o preço de sua passagem será de R${passagem2:.2f}")

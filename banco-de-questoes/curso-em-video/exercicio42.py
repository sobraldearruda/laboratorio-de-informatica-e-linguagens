# Exercício 42 - Analisando Triângulos 2.0

reta1 = float(input("Primeiro segmento: "))
reta2 = float(input("Segundo segmento: "))
reta3 = float(input("Terceiro segmento: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
  print("Os segmentos acima podem formar um triângulo ", end="")
  if reta1 == reta2 == reta3:
    print("equilátero.")
  elif reta1 != reta2 != reta3 != reta1:
    print("escaleno.")
  else:
    print("isósceles.")
else:
  print("Os segmentos acima não podem formar triângulo.")

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Cálculo da hipotenusa

import math

cathetus1 = float(input("Medida do Cateto 1? "))
cathetus2 = float(input("Medida do Cateto 2? "))
hypotenuse = math.sqrt((cathetus1 ** 2) + (cathetus2 ** 2))
print(f"Medida da Hipotenusa: {hypotenuse:.2f}")

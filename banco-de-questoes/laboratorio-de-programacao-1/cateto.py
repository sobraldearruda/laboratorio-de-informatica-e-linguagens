## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Cateto

import math

hypotenuse = float(input("hipotenusa? "))
cathetus1 = float(input("cateto? "))
cathetus2 = math.sqrt(hypotenuse ** 2 - cathetus1 ** 2)
print(f"hipotenusa: {hypotenuse:.2f}")
print(f"cateto 1: {cathetus1:.2f}")
print(f"cateto 2: {cathetus2:.2f}")

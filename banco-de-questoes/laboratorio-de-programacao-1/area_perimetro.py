## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Área e perímetro de um círculo

import math

diameter = int(input())
radius = diameter / 2
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius
print(f"A: {area:.5f}")
print(f"P: {perimeter:.5f}")

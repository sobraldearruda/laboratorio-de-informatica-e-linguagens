## UFCG
## Ciência da Computação
## Programação I / Laboratório de programação I
## Rafael de Arruda Sobral
## Quadrado na circunferência

import math

radius = float(input())
circle_area = math.pi * radius ** 2
square_side = radius * math.sqrt(2)
square_area = square_side * square_side
noncommon_area = circle_area - square_area
print(f"Área não comum: {noncommon_area:.5f}")

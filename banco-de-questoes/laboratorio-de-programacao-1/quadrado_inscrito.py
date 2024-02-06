## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Quadrado inscrito na circunferência

import math

side = float(input())
radius = side / math.sqrt(2)
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"Perímetro: {perimeter:.5f}")
print(f"Área: {area:.5f}")

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Perímetro de Triângulo

import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
d1 = math.sqrt (((x1 - x2) ** 2) + ((y1 - y2) ** 2))
d2 = math.sqrt (((x2 - x3) ** 2) + ((y2 - y3) ** 2))
d3 = math.sqrt (((x3 - x1) ** 2) + ((y3 - y1) ** 2))
perimeter = d1 + d2 + d3
print(f"O perímetro é de {perimeter:.2f}")

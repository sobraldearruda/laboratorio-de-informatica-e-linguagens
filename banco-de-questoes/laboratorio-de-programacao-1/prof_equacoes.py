## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Prof Equações

import math

a = int(input())
b = int(input())
c = int(input())
delta = (b ** 2) - (4 * a * c)
if delta > 0:
    x = math.sqrt(delta)
    x1 = (- b + x) / (2 * a)
    x2 = (- b - x) / (2 * a)
    print(f"x1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}")
elif delta < 0:
    print("sem raizes reais")
elif delta == 0:
    x = - b / (2 * a)
    print(f"x = {x:.2f}")

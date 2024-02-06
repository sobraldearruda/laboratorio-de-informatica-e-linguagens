## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Controle de Água

import math

speed = float(input())
diameter = float(input())
time = float(input())
section = math.pi * ((diameter / 2) ** 2)
flow = speed * section * 1000
water = time * flow
print(f"Quantidade de água = {water:.2f} litros.")

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Área do cilindro

import math

print("Cálculo da Superfície de um Cilindro\n---")
diameter = float(input("Medida do diâmetro? "))
height = float(input("Medida da altura? "))
radius = diameter / 2
area = (2 * (math.pi * radius ** 2)) + (2 * math.pi * radius * height)
print(f"---\nÁrea calculada: {area:.2f}")

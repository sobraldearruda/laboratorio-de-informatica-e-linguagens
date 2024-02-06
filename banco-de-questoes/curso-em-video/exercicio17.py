# Exercício 17 - Catetos e Hipotenusa

import math

oposto = float(input("Comprimento do cateto oposto: "))
adjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = math.hypot(oposto, adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")

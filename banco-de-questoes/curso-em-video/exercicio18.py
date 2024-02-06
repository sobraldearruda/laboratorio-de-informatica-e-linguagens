# Exercício 18 - Seno, Cosseno, Tangente

import math

angulo = float(input("Digite o ângulo que você deseja: "))
print(f"O ângulo de {angulo:.1f} tem o seno de {math.sin(math.radians(angulo)):.2f}")
print(f"O ângulo de {angulo:.1f} tem o cosseno de {math.cos(math.radians(angulo)):.2f}")
print(f"O ângulo de {angulo:.1f} tem a tangente de {math.tan(math.radians(angulo)):.2f}")

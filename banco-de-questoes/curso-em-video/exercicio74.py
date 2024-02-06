# Exercício 74 - Maior e Menor Valores em Tupla

import random

sorteio = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10),
           random.randint(1, 10), random.randint(1, 10))
print(f"Os valores sorteados foram: {sorteio}")
print(f"O maior valor sorteado foi {max(sorteio)}")
print(f"O menor valor sorteado foi {min(sorteio)}")

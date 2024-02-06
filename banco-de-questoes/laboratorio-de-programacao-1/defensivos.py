## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Defensivos

import math

product = input()
area = float(input())
if product == "Fungicida":
    amount = math.ceil((area * 1.0) / 50)
    price = amount * 320
    print(f"{amount} Fungicida(s). {price:.2f} reais.")
elif product == "Inseticida":
    amount = math.ceil((area * 2.5) / 30)
    price = amount * 400
    print(f"{amount} Inseticida(s). {price:.2f} reais.")
elif product == "Herbicida":
    amount = math.ceil((area * 0.3) / 1)
    price = amount * 100
    print(f"{amount} Herbicida(s). {price:.2f} reais.")

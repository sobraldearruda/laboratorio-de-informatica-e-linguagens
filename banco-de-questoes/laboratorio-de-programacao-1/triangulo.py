## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## É triângulo

side1 = int(input())
side2 = int(input())
side3 = int(input())
if ((side2 - side3) < side1 < (side2 + side3)) or ((side1 - side3) < side2 < (side1 + side3)) or ((side1 - side2) < side3 < (side1 + side2)):
    perimeter = side1 + side2 + side3
    print(f"triangulo valido. {perimeter}")
else:
    print("triangulo invalido.")

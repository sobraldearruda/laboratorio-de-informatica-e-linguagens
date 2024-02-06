## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Ciclo trigonométrico

angle = float(input())
if (angle == 0) or (angle % 90 == 0) or (angle % 180 == 0) or (angle % 270 == 0) or (angle % 360 == 0):
    print("Sobre eixos")
elif angle > 0 and angle < 90:
    print("Quadrante 1")
elif angle > 90 and angle < 180:
    print("Quandrante 2")
elif angle > 180 and angle < 270:
    print("Quadrante 3")
elif angle > 270 and angle < 360:
    print("Quadrante 4")
elif angle > 360:
    total = angle // 360
    rest = angle - (total * 360)
    if rest > 0 and rest < 90:
        print("Quadrante 1")
    elif rest > 90 and rest < 180:
        print("Quadrante 2")
    elif rest > 180 and rest < 270:
        print("Quadrante 3")
    elif rest > 270 and rest < 360:
        print("Quadrante 4")

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Plif Plof

n1 = int(input())
n2 = int(input())
n3 = int(input())
calculus = n1 + n2 + n3
if (calculus % 3 == 0) and (calculus % 5 == 0):
    print("plifplof")
elif calculus % 3 == 0:
    print("plif")
elif calculus % 5 == 0:
    print("plof")
else:
    print(calculus)

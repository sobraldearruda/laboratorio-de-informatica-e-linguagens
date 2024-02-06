## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Com ou sem duplicados

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
if (n1 == n2) or (n1 == n3) or (n1 == n4) or (n1 == n5) or (n2 == n3) or (n2 == n4) or (n2 == n5) or (n3 == n4) or (n3 == n5) or (n4 == n5):
    print("com duplicados")
else:
    print("sem duplicados")

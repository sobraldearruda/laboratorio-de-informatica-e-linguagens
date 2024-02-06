## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Segundo

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
if n1 <= n2 <= n3 <= n4:
    small = n2
    big = n3
elif n1 <= n2 <= n4 <= n3:
    small = n2
    big = n4
elif n1 <= n3 <= n2 <= n4:
    small = n3
    big = n2
elif n1 <= n3 <= n4 <= n2:
    small = n3
    big = n4
elif n1 <= n4 <= n2 <= n3:
    small = n4
    big = n2
elif n1 <= n4 <= n3 <= n2:
    small = n4
    big = n3
elif n2 <= n1 <= n3 <= n4:
    small = n1
    big = n3
elif n2 <= n1 <= n4 <= n3:
    small = n1
    big = n4
elif n2 <= n3 <= n1 <= n4:
    small = n3
    big = n1
elif n2 <= n3 <= n4 <= n1:
    small = n3
    big = n4
elif n2 <= n4 <= n1 <= n3:
    small = n4
    big = n1
elif n2 <= n4 <= n3 <= n1:
    small = n4
    big = n3
elif n3 <= n1 <= n2 <= n4:
    small = n1
    big = n2
elif n3 <= n1 <= n4 <= n2:
    small = n1
    big = n4
elif n3 <= n2 <= n1 <= n4:
    small = n2
    big = n1
elif n3 <= n2 <= n4 <= n1:
    small = n2
    big = n4
elif n3 <= n4 <= n1 <= n2:
    small = n4
    big = n1
elif n3 <= n4 <= n2 <= n1:
    small = n4
    big = n2
elif n4 <= n1 <= n2 <= n3:
    small = n1
    big = n2
elif n4 <= n1 <= n3 <= n2:
    small = n1
    big = n3
elif n4 <= n2 <= n1 <= n3:
    small = n2
    big = n1
elif n4 <= n2 <= n3 <= n1:
    small = n2
    big = n3
elif n4 <= n3 <= n1 <= n2:
    small = n3
    big = n1
elif n4 <= n3 <= n2 <= n1:
    small = n3
    big = n2
print(f"Considerando os números {n1}, {n2}, {n3} e {n4}")
print(f"O segundo menor número é {small}")
print(f"O segundo maior número é {big}")

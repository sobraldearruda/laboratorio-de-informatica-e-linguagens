## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Encontra elemento

num = input()
numbers = input().split()
count = 0
for n in numbers:
    if num == n:
        count += 1
if count > 0:
    print("sim")
else:
    print("não")

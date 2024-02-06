## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Posições elemento

num = int(input())
sequence = input().split()
position = []
for s in range(len(sequence)):
    sequence[s] = int(sequence[s])
for e in range(len(sequence)):
    if num == sequence[e]:
        position.append(e)
if position == []:
    print("-1")
else:
    for p in position:
        if p != position[-1]:
            print(p, end=" ")
        else:
            print(p)

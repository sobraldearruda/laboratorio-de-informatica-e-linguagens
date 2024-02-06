## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Múltiplos de cinco

num = int(input())
while True:
    for n in range(5, num):
        if n % 10 == 0 and n != 5:
            print(n)
    break

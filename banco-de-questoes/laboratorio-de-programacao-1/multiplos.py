## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Múltiplos do primeiro

num = int(input())
mult = 0
for n in range(0, 10):
    numbers = int(input())
    if numbers % num == 0:
        mult = mult + numbers
print(mult)

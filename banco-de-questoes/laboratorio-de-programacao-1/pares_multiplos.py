## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Pares de múltiplos

numbers = input()
num = int(input())
pairs = []
for n in range(len(numbers)):
    if numbers[n] * num == numbers[n+1]:
        pairs.append(numbers[n])
        pairs.append(numbers[n+1])
print(pairs)

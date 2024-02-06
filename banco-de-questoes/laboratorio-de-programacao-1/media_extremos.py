## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Média dos extremos

num = int(input())
numbers = []
for n in range(num):
    numbers.append(int(input()))
lower = numbers[0]
higher = numbers[0]
for u in numbers:
    if u < lower:
        lower = u
    elif u > higher:
        higher = u
print(f"Menor número: {lower}")
print(f"Maior número: {higher}")
average = (lower + higher) / 2
print(f"Média dos extremos: {average:.2f}")
low = 0
high = 0
for m in numbers:
    if m < average:
        low += 1
    elif m > average:
        high += 1
print(f"{low} número(s) abaixo da média")
print(f"{high} número(s) acima da média")

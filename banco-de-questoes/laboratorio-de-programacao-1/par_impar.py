## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Par e ímpar

num = int(input())
numbers = []
even1 = 0
even2 = 0
odd1 = 0
odd2 = 0
for n in range(num):
    numbers.append(int(input()))
for n in numbers:
    if n % 2 == 0:
        even1 += n
        even2 += 1
    elif n % 2 != 0:
        odd1 += n
        odd2 += 1
print(f"pares: {even2}")
print(f"ímpares: {odd2}")
print(f"média pares: {even1 / even2:.1f}")
print(f"média ímpares: {odd1 / odd2:.1f}")

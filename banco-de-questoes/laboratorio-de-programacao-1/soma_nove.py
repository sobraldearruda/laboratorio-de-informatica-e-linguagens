## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Soma 999

count = 0
average = 0
bigger = 0
numbers = []
while True:
    num = int(input())
    numbers.append(num)
    count += num
    if count >= 999: break
average = count / len(numbers)
for n in numbers:
    if n > average:
        bigger += 1
print(count)
print(f"{average:.2f}")
print(bigger)

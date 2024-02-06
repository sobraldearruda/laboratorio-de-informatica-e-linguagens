## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Produto posições

num = input()
even = 0
odd = 0
for n in range(len(num)):
  if n % 2 == 0:
    even += int(num[n])
  else:
    odd += int(num[n])
mult = even * odd
print(f'{mult:05.0f}')

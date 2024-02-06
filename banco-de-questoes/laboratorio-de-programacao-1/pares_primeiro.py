## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Pares primeiro

def pares_primeiro(lista):
  new = []
  for num in lista:
    if num % 2 == 0:
      new.append(num)
  for num in lista:
    if num % 2 != 0:
      new.append(num)
  return new

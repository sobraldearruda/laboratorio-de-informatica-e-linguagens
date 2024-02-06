## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Octal/Decimal

number = input()
count = len(number)-1
add = 0
for n in number:
  convertion = int(n) * (8 ** count)
  print(f"{n} * 8^{count} = {convertion}")
  count = count -1
  add = add + convertion
print(f"{number}(8) = {add}(10)")

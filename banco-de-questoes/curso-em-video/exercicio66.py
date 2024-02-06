# Exercício 66 - Vários Números com Flag

cont = 0
total = 0
while True:
  num = int(input("Digite um número [999 para parar]: "))
  cont += 1
  total += num
  if num == 999:
    cont -= 1
    total -= 999
    break
print(f"Você digitou {cont} números e a soma entre eles foi {total}.")

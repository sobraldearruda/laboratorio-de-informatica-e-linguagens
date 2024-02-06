# Exercício 64 - Tratando Vários Valores

cont = 0
total = 0
while total < 999:
  num = int(input("Digite um número [999 para parar]: "))
  cont += 1
  total += num
  if num == 999:
    cont -= 1
    total -= 999
    break
print(f"Você digitou {cont} números e a soma entre eles foi {total}.")

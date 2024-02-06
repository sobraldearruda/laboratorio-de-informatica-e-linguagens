# Exercício 67 - Tabuada 3.0

while True:
  print("-" * 30)
  num = int(input("Quer ver a tabuada de qual valor? "))
  print("-" * 30)
  if num < 0:
    print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")
    break
  else:
    for n in range(1, 11):
      print(f"{num} x {n:2} = {num*n}")

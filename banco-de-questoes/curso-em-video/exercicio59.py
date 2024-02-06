# Exercício 59 - Criando um Menu de Opções

num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))
opcao = 0
while opcao != 5:
  print('''
  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa''')
  opcao = int(input(">>> Qual é a sua opção? "))
  if opcao == 1:
    print(f"A soma entre {num1} + {num2} é igual a {num1 + num2}.")
  elif opcao == 2:
    print(f"O produto de {num1} x {num2} é igual a {num1 * num2}.")
  elif opcao == 3:
    if num1 > num2:
      print(f"{num1} é maior que {num2}.")
    elif num1 < num2:
      print(f"{num2} é maior que {num1}.")
    else:
      print(f"Os números {num1} e {num2} são iguais.")
  elif opcao == 4:
    print("Informe os números novamente.")
    num1 = float(input("Primeiro valor: "))
    num2 = float(input("Segundo valor: "))
  elif opcao == 5:
    print("Finalizando...")
  else:
    print("Opção inválida. Tente novamente.")
print("Fim do programa! Volte sempre!")

# Exercício 36 - Aprovando Empréstimo

casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador? R$"))
anos = int(input("Quantos anos de financiamento? "))
prestaçao = casa / (anos * 12)
porcentagem = (salario * 30) / 100
print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestaçao:.2f}.")
if prestaçao <= porcentagem:
  print("Empréstimo pode ser concedido!")
else:
  print("Empréstimo negado!")

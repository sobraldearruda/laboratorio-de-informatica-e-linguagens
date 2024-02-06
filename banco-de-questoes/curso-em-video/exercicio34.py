# Exercício 34 - Aumentos Múltiplos

salario = float(input("Qual é o salário do funcionário? R$"))
if salario > 1250.00:
  aumento = (salario * 10) / 100
else:
  aumento = (salario * 15) / 100
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${salario + aumento:.2f} agora.")

# Exercício 13 - Reajuste Salarial

salario = float(input("Qual é o salário do funcionário? R$"))
aumento = float(input("Quantos porcento de aumento? "))
porcentagem = salario * aumento / 100
print(f"Um funcionário que ganhava R${salario:.2f}, 
      com {aumento:.2f}% de aumento, passa a receber R${salario+porcentagem:.2f}.")

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Reajuste do salário mínimo

current_value = float(input("Valor atual? "))
new_value = float(input("Novo valor? "))
readjustment = new_value - current_value
percentage = (readjustment * 100) / current_value
print(f"Reajuste de {percentage:.1f}%")

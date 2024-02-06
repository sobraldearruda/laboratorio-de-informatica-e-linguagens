## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Salário

gross_salary = float(input())
working_time = int(input())
earning = gross_salary / working_time
ir = gross_salary * 0.11
inss = gross_salary * 0.08
union = gross_salary * 0.05
net_salary = gross_salary - (ir + inss + union)
net_time = net_salary / working_time
print(f"Salário Bruto = {gross_salary:.2f}")
print(f"Hora Bruta = {earning:.2f}")
print(f"Desconto IR = {ir:.2f}")
print(f"Desconto INSS = {inss:.2f}")
print(f"Desconto Sindicato = {union:.2f}")
print(f"Salário Líquido = {net_salary:.2f}")
print(f"Hora Líquida = {net_time:.2f}")

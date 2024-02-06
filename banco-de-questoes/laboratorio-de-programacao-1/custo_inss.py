## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Custo INSS

salary = float(input())
employer = salary - (salary - (salary * 12) / 100)
if salary <= 1317.07:
    percent1 = salary - (salary - (salary * 8) / 100)
    print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {employer:.2f}")
    print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {percent1:.2f}")
elif salary > 1317.08 and salary < 2195.12:
    percent2 = salary - (salary - (salary * 9) / 100)
    print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {employer:.2f}")
    print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {percent2:.2f}")
else:
    percent3 = salary - (salary - (salary * 11) / 100)
    print(f"O valor da contribuição do INSS a ser pago pelo empregador é de R$ {employer:.2f}")
    print(f"O valor da contribuição do INSS a ser pago pelo empregado é de R$ {percent3:.2f}")

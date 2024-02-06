## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Formata CPF

cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())
digit1 = cpf1 % 100
digit2 = cpf2 % 100
digit3 = cpf3 % 100
new_cpf1 = (cpf1 - digit1) // 100
new_cpf2 = (cpf2 - digit2) // 100
new_cpf3 = (cpf3 - digit3) // 100
sum_digit1 = (digit1 // 10) + (digit1 % 10)
sum_digit2 = (digit2 // 10) + (digit2 % 10)
sum_digit3 = (digit3 // 10) + (digit3 % 10)
print('{:09d}-{:02d}'.format(new_cpf1, digit1))
print(sum_digit1)
print('{:09d}-{:02d}'.format(new_cpf2, digit2))
print(sum_digit2)
print('{:09d}-{:02d}'.format(new_cpf3, digit3))
print(sum_digit3)

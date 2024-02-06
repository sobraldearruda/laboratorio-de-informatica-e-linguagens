## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Dígito verificador de 5 dígitos

num = input()
n1 = int(num[0])
n2 = int(num[1])
n3 = int(num[2])
n4 = int(num[3])
n5 = int(num[4])
check_digit = (n1 + n2 + n3 + n4 + n5) % 11
check_digit_format = (f"{check_digit:02.0f}")
check_digit_str = str(check_digit_format)
print(num + "-" + check_digit_str)

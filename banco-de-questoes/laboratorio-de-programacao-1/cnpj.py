## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## CNPJ

root = input()
unit = "/0001"
num1 = int(root[0])
num2 = int(root[1])
num3 = int(root[3])
num4 = int(root[4])
num5 = int(root[5])
num6 = int(root[7])
num7 = int(root[8])
num8 = int(root[9])
num9 = int(unit[1])
num10 = int(unit[2])
num11 = int(unit[3])
num12 = int(unit[4])
digit = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12
matrix = root + unit + "-" "{:02.0f}".format(digit)
print(matrix)

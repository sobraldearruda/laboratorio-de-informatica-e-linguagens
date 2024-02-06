## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Dígitos de verificação do CPF

def calcula_digitos_verificacao(num):
    count1 = 0
    count2 = 0
    count1 += int(num[8]) * 2
    count1 += int(num[7]) * 3
    count1 += int(num[6]) * 4
    count1 += int(num[5]) * 5
    count1 += int(num[4]) * 6
    count1 += int(num[3]) * 7
    count1 += int(num[2]) * 8
    count1 += int(num[1]) * 9
    count1 += int(num[0]) * 10
    digit1 = (count1 * 10) % 11
    if digit1 == 10:
        digit1 = 0
    count2 += digit1 * 2
    count2 += int(num[8]) * 3
    count2 += int(num[7]) * 4
    count2 += int(num[6]) * 5
    count2 += int(num[5]) * 6
    count2 += int(num[4]) * 7
    count2 += int(num[3]) * 8
    count2 += int(num[2]) * 9
    count2 += int(num[1]) * 10
    count2 += int(num[0]) * 11
    digit2 = (count2 * 10) % 11
    if digit2 == 10:
        digit2 = 0
    string = str(digit1) + str(digit2)
    return(string)

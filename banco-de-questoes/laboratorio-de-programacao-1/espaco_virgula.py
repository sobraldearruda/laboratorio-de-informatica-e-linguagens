## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Espaço por vírgula

statement = input()
num1 = int(input())
num2 = int(input())
position = 1
new = ""
for s in statement:
    if num1 < position <= num2:
        if s == " ":
            new += ","
        else:
            new += s
        if position != num2:
            new += " "
    position += 1
print(new)

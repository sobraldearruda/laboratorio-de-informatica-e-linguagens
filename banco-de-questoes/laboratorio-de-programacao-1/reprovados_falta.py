## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Reprovados por falta

failed = 0
while True:
    attendance = input()
    if attendance == "-":
        break
    l = -1
    count = 0
    while l < int(len(attendance) - 1):
        l += 1
        if attendance[l] == "f":
            count += 1
    if count > 8:
        failed += 1
print(f"{failed} aluno(s) reprovado(s) por falta.")

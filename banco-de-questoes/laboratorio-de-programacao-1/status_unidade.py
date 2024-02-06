## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Status unidade

tests = int(input())
if tests == 1:
    score1 = float(input())
    print(f"{score1:.1f}")
    print("Aluno ainda não aprovado na unidade")
elif tests == 2:
    score1 = float(input())
    score2 = float(input())
    average2 = (score1 + score2) / 2
    print(f"{average2:.1f}")
    if average2 < 6.0:
        print("Aluno ainda não aprovado na unidade")
    elif average2 >= 6.0:
        print("Aluno aprovado na unidade")
elif tests == 3:
    score1 = float(input())
    score2 = float(input())
    score3 = float(input())
    average3 = ((score1 + score2 + score3) / 3) - 0.5
    print(f"{average3:.1f}")
    if average3 < 6.0:
        print("Aluno ainda não aprovado na unidade")
    elif average3 >= 6.0:
        print("Aluno aprovado na unidade")
elif tests == 4:
    score1 = float(input())
    score2 = float(input())
    score3 = float(input())
    score4 = float(input())
    average4 = ((score1 + score2 + score3 + score4) / 4) - 0.5
    print(f"{average4:.1f}")
    if average4 < 6.0:
        print("Aluno ainda não aprovado na unidade")
    elif average4 >= 6.0:
        print("Aluno aprovado na unidade")

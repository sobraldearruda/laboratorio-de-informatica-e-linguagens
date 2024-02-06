## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Status

score1 = float(input())
score2 = float(input())
score3 = float(input())
classes = int(input())
average = (score1 + score2 + score3) / 3
absence = (classes * 100) / 30
if average >= 7 and absence < 25:
    print("aprovado por media")
elif absence > 25:
    print("reprovado por faltas")
elif average < 4:
    print("reprovado por nota")
elif average < 7 and average > 4 and absence < 25:
    print("prova final")

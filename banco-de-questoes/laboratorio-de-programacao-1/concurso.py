## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Concurso

score1 = float(input())
score2 = float(input())
score3 = float(input())
age1 = int(input())
score_1 = float(input())
score_2 = float(input())
score_3 = float(input())
age_2 = int(input())
candidate1 = (score1 * 0.3) + (score2 * 0.4) + (score3 * 0.3)
candidate2 = (score_1 * 0.3) + (score_2 * 0.4) + (score_3 * 0.3)
if candidate1 > candidate2:
    print(f"O primeiro candidato foi aprovado com média {candidate1:.1f}.")
elif candidate1 < candidate2:
    print(f"O segundo candidato foi aprovado com média {candidate2:.1f}.")
elif candidate1 == candidate2:
    if age1 > age_2:
        print(f"O primeiro candidato foi aprovado com média {candidate1:.1f}.")
    elif age1 < age_2:
        print(f"O segundo candidato foi aprovado com média {candidate2:.1f}.")
    elif age1 == age_2:
        print("Empate.")

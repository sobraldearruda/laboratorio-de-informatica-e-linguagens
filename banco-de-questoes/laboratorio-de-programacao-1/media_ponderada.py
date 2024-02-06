## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Média Ponderada

score1 = float(input())
score2 = float(input())
score3 = float(input())
weight1 = float(input())
weight2 = float(input())
weight3 = 100 - (weight1 + weight2)
score1_weighted = (score1 * weight1) / 100
score2_weighted = (score2 * weight2) / 100
score3_weighted = (score3 * weight3) / 100
average = score1_weighted + score2_weighted + score3_weighted
print(f"Média Final: {average:.1f}")

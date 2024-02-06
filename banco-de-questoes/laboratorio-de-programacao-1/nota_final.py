## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Nota na final

print("== Estágio 1 ==")
weight1 = float(input("Peso? "))
score1 = float(input("Nota? "))
print("== Estágio 2 ==")
weight2 = float(input("Peso? "))
score2 = float(input("Nota? "))
print("== Estágio 3 ==")
weight3 = float(input("Peso? "))
score3 = float(input("Nota? "))
average = (score1 * weight1) + (score2 * weight2) + (score3 * weight3)
final_average1 = (5.0 - (average * 0.6)) / 0.4
final_average2 = (7.0 - (average * 0.6)) / 0.4
print("== Resultados ==")
print(f"Média parcial: {average:.1f}")
print(f"Nota na final, pra média 5.0 = {final_average1:.1f}")
print(f"Nota na final, pra média 7.0 = {final_average2:.1f}")

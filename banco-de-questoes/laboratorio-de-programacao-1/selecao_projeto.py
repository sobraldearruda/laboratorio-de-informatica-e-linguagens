## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Seleção Projeto

cre = float(input())
experience = int(input())
interview = float(input())
if cre < 7.0 and experience < 6:
    print("Candidato eliminado. CRE e experiência abaixo do limite.")
elif cre < 7.0 and experience >= 6:
    print("Candidato eliminado. CRE abaixo do limite.")
elif cre >= 7.0 and experience < 6:
    print("Candidato eliminado. Experiência abaixo do limite.")
elif (cre >= 7.0 and experience >= 6) and (interview <= 3):
    print("Candidato classificado.")
elif (cre >= 7.0 and experience >= 6) and (interview > 3):
    print("Candidato aprovado.")

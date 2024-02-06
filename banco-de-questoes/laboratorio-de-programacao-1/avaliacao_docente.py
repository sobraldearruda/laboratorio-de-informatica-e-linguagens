## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Avaliação docente

semesters = int(input())
teaching = float(input())
production = float(input())
coordination = float(input())
administration = float(input())
average = (teaching + production + coordination + administration) / semesters
if semesters < 4:
    print("Promoção indeferida. Número de semestres insuficiente.")
elif semesters >= 4:
    if teaching >= 320 and production >= 100 and coordination >= 20 and average >= 140:
        print("Promoção deferida. Parabéns!")
    elif teaching < 320 or production < 100 or coordination < 20:
        print("Promoção indeferida. Pontuação mínima não alcançada.")
    elif average < 140:
        print("Promoção indeferida. Média insuficiente.")

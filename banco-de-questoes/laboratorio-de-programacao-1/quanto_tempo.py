## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Quanto tempo

def quanto_tempo(horario1, horario2):
    time1 = int(horario1[0] + horario1[1])
    minute1 = int(horario1[3] + horario1[4])
    time2 = int(horario2[0] + horario2[1])
    minute2 = int(horario2[3] + horario2[4])
    time1 = (time1 * 60) + minute1
    time2 = (time2 * 60) + minute2
    rest = time2 - time1
    time = (rest // 60)
    minute = (rest % 60)
    return(f"{time} hora(s) e {minute} minuto(s)")

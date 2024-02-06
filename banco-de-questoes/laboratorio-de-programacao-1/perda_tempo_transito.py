## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Perda de Tempo no Trânsito

day1 = int(input())
day2 = int(input())
day3 = int(input())
day4 = int(input())
day5 = int(input())
minutes = day1 + day2 + day3 + day4 + day5
minutes_average = minutes / 5
percentage = (minutes * 100) / 7200
episodes = minutes // 50
print(f"Você perdeu {minutes:.0f} min na semana (média de {minutes_average:.1f} min por dia).")
print(f"Isso significa {percentage:.2f}% da sua semana produtiva.")
print(f"Daria para assistir {episodes:.0f} episódio(s) de House.")

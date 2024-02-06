## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Consumo de energia

power = int(input())
minutes = int(input())
kwh = power / 1000
hours = minutes / 60
usage = kwh * hours
print(f"{usage:.1f} kWh")

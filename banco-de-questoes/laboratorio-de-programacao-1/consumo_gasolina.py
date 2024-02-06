## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Consumo de gasolina

initial_position = float(input())
initial_litres = float(input())
final_position = float(input())
final_litres = float(input())
distance = final_position - initial_position
usage = initial_litres - final_litres
print("{:.1f}".format(distance / usage))

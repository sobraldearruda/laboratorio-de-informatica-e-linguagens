## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Conversão para Graus Decimais

degrees = int(input())
minutes = int(input())
seconds = int(input())
value = degrees + ((minutes / 60.0) + (seconds / 3600.0))
print(f"graus = {value:.4f}")

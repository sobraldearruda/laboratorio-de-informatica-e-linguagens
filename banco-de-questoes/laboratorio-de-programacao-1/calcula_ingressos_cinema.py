## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Calcula ingressos do cinema

adults = int(input())
children = int(input())
ticket = float(input())
price = (adults * ticket) + (children * (ticket / 2))
print(f"Total: R$ {price:.2f}")

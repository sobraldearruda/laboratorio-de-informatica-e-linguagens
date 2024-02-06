## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Autorização voos

available = int(input())
amount = int(input())
flights = 0
for a in range(amount):
    time = int(input())
    if time <= available:
        available = available - time
        flights += 1
print(f"{flights} voo(s) autorizados.")

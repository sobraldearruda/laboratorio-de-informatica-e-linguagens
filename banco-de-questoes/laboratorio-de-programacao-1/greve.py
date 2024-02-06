## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Greve

abstention = int(input())
favor = int(input())
against = int(input())
total = abstention + favor + against
abstention_percent = (abstention * 100) / total
favor_percent = (favor * 100) / total
against_percent = (against * 100) / total
print("Resultado da Votação")
print(f"\n{abstention} abstenções ({abstention_percent:.2f}%)")
print(f"{favor} a favor ({favor_percent:.2f}%)")
print(f"{against} contra ({against_percent:.2f}%)")

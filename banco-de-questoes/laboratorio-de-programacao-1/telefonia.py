## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Telefonia

time = int(input())
if time <= 3:
    tax1 = (time * 0.50) + 1
    print(f"R$ {tax1:.2f}")
elif time > 3:
    tax2 = (((time // 5) * 3) + 1) + ((time % 5) * 0.70)
    print(f"R$ {tax2:.2f}")

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Pedágio

vehicle = input()
if vehicle == "Automóvel utilitário":
    print("Valor a pagar: R$ 11.40.")
elif vehicle == "Ônibus":
    axis = int(input())
    tax = axis * 11.40
    print(f"Valor a pagar: R$ {tax:.2f}.")
elif vehicle == "Caminhão":
    axis = int(input())
    tax = axis * 9.60
    print(f"Valor a pagar: R$ {tax:.2f}.")
elif vehicle == "Motocicleta":
    print("Valor a pagar: R$ 5.70.")
else:
    print("Veículo não cadastrado.")

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Limpeza

service = input()
if service == "1":
    tank = int(input())
    budget = tank * 80
    if budget >= 200:
        print(f"R$ " + str(budget) + ",00")
        print("Brinde!")
    elif budget < 200:
        print(f"R$ " + str(budget) + ",00")
elif service == "2":
    tank = int(input())
    budget = tank * 50
    if budget >= 200:
        print(f"R$ " + str(budget) + ",00")
        print("Brinde!")
    elif budget < 200:
        print(f"R$ " + str(budget) + ",00")
elif service == "3":
    print("R$ 50,00")

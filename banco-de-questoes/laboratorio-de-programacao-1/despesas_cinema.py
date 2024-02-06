## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Calcula Despesas do Cinema

budget = float(input("Orçamento? R$ "))
adults_num = int(input("Número de adultos? "))
children_num = int(input("Número de crianças? "))
pizza = float(input("Preço da pizza? R$ "))
soda = float(input("Preço do refrigerante? R$ "))
parking = float(input("Preço do estacionamento? R$ "))
ticket = float(input("Preço do ingresso do cinema? R$ "))
eating = pizza + soda
adults = adults_num * (ticket + 2)
children = children_num * ((ticket / 2) + 2)
cinema = adults + children
total = eating + cinema + parking
person = total / (adults_num + children_num)
outcome = budget - total
print("========== Despesas do cinema ==========")
print(f"Alimentacao: R$ {eating:.2f}")
print(f"Cinema: R$ {cinema:.2f}")
print(f"Custo médio por pessoa: R$ {person:.2f}")
print(f"Total: {total:.2f}")
print(f"Saldo após passeio: {outcome:.2f}")

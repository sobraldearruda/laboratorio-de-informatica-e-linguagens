## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Caixa preta

weight = 0
fuel = 0
height = 0
while True:
    data = input()
    num = data.split()
    if int(num[0]) < 0:
        print("dado inconsistente. peso negativo.")
        break
    if int(num[1]) < 0:
        print("dado inconsistente. combustível negativo.")
        weight += 1
        break
    if int(num[2]) < 0:
        print("dado inconsistente. altitude negativa.")
        weight += 1
        fuel += 1
        break
    if int(num[0]) >= 0:
        weight += 1
    if int(num[1]) >= 0:
        fuel += 1
    if int(num[2]) >= 0:
        height += 1
print(f"peso: {weight}")
print(f"combustível: {fuel}")
print(f"altitude: {height}")

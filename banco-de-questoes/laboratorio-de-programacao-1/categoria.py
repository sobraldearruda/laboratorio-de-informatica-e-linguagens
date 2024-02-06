## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Categoria

name = input()
age = int(input())
if age >= 5 and age <= 7:
    print(f"{name}, {age} anos, Infantil A.")
elif age >= 8 and age <= 10:
    print(f"{name}, {age} anos, Infantil B.")
elif age >= 11 and age <= 13:
    print(f"{name}, {age} anos, Juvenil A.")
elif age >= 14 and age <= 17:
    print(f"{name}, {age} anos, Juvenil B.")
elif age >= 18:
    print(f"{name}, {age} anos, Senior.")
else:
    print(f"{name}, {age} anos, Não pode competir.")

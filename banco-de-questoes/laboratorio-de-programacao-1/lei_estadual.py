## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Lei Estadual

age = int(input("Idade? "))
if age < 12:
    print("criança (meia entrada)")
elif age >= 65:
    print("idoso (meia entrada)")
elif age < 65 and age >= 12:
    student = input("Estudante? ")
    if student == "s":
        public = input("Rede Pública? ")
        if public == "s":
            print("estudante da rede pública (isento)")
        elif public == "n":
            print("estudante (meia entrada)")
    elif student == "n":
        print("adulto (inteira)")

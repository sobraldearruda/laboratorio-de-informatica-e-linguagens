## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Troca coincidentes

statement = input()
key = list(input())
decode = ""
for s in range(len(statement)):
    if statement[s] == str(s):
        decode += key[s]
    else:
        decode += statement[s]
print(decode)

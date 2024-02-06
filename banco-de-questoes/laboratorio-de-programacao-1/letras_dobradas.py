## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Letras dobradas

n = int(input())
normais = 0
normal = []
dobradas = 0
dobrada = []
palavras = []
for i in range(n):
    palavras.append(input())
for y in range(len(palavras)):
    palavra = palavras[y]
    repetido = False
    for x in range((len(palavra) -1)):
        if palavra[x] == palavra[x+1] and repetido == False:
            dobradas += 1
            repetido = True
            dobrada.append(palavra)
            break
    if repetido == False:
            normais += 1
            normal.append(palavra)
print(f"{dobradas:d} palavra(s) com letras dobradas:")
for z in range(len(dobrada)):
    print(dobrada[z])
print("---")
print(f"{normais:d} palavra(s) sem letras dobradas:")
for w in range(len(normal)):
    print(normal[w])

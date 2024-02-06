## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Letras alternadas

word = input()
alternate = ""
for i in range(0, len(word), 2):
    alternate = alternate + word[i]
print(alternate)

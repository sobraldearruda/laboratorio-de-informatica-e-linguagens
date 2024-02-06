## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Nova palavra

word = input()
num = int(input())
new = ""
for w in range(len(word)):
    new += word[w]
    repetition = num % 10
    new += word[w] * repetition
    num = num // 10
print(new)

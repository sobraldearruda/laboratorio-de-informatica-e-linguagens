## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Forma palavra

word1 = input()
word2 = input()
word3 = input()
words = ""
for w in range(len(word1)):
    if word1[w] >= word2[w] >= word3[w]:
        words += word1[w]
    elif word1[w] >= word3[w] >= word2[w]:
        words += word1[w]
    elif word2[w] >= word1[w] >= word3[w]:
        words += word2[w]
    elif word2[w] >= word3[w] >= word1[w]:
        words += word2[w]
    elif word3[w] >= word1[w] >= word2[w]:
        words += word3[w]
    elif word3[w] >= word2[w] >= word1[w]:
        words += word3[w]
print(words)

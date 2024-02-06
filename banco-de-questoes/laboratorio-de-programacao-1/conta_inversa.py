## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Conta inversa

word = input()
contrary = ""
equal = 0
for w in range(len(word) -1, -1, -1):
    contrary += word[w]
for c in range(len(word)):
    if contrary[c] == word[c]:
        equal += 1
print(f"A palavra {word} contém {equal} caractere(s) coincidente(s) com a sua inversa.")

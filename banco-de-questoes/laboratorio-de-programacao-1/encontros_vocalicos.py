## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Encontros vocálicos

n = int(input())
words = []
count = 0
for w in range(n):
    words.append(input())
for o in words:
    for r in range(0, len(o) -1):
        if (o[r] == "a" or o[r] == "e" or o[r] == "i" or o[r] == "o" or o[r] == "u") and (o[r+1] == "a" or o[r+1] == "e" or o[r+1] == "i" or o[r+1] == "o" or o[r+1] == "u"):
            count += 1
print(f"com: {count}")
print(f"sem: {n-count}")

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Árvore de natal

num = int(input())
top_down = "o"
letter = "o"
ratio = 2
space = num
print(f"{top_down:>{num}s}")
for n in range(num - 1):
    letter = letter + (top_down * ratio)
    space += 1
    print(f"{letter:>{space}s}")
print(f"{top_down:>{num}s}")

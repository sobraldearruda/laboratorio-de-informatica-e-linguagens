## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Controle de qualidade

frozen = float(input())
unfrozen = float(input())
percent = ((frozen - unfrozen) * 100) / frozen
print(f"{percent:.1f}% do peso do produto é de água congelada.")
if percent < 5:
    print("Produto qualis A.")
elif percent < 10:
    print("Produto em conformidade.")
else:
    print("Produto não conforme.")

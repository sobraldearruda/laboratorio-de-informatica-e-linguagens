# Exercício 26 - Primeira e última ocorrência de uma string

frase = str(input("Digite uma frase: ")).lower().strip()
print(f"A letra A aparece {frase.count('a')} vezes na frase.")
print(f"A primeira letra A apareceu na posição {frase.find('a') + 1}.")
print(f"A última letra A apareceu na posição {frase.rfind('a') + 1}")

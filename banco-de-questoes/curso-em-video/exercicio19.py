# Exercício 19 - Sorteando um item na lista

import random

aluno1 = input("Primeiro aluno: ")
aluno2 = input("Segundo aluno: ")
aluno3 = input("Terceiro aluno: ")
aluno4 = input("Quarto aluno: ")
lista = [aluno1, aluno2, aluno3, aluno4]
print(f"O aluno escolhido foi {random.choice(lista)}.")

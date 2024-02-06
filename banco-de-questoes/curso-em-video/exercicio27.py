# Exercício 27 - Primeiro e último nome de uma pessoa

nome = input("Digite seu nome completo: ").strip().split()
print("Prazer em te conhecer!")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[-1]}")

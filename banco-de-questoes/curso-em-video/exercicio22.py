# Exercício 22 - Analisador de Textos

nome = input("Digite seu nome completo: ").strip()
print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
nomes = nome.split()
print(f"Seu primeiro nome é {nomes[0]} e ele tem {len(nomes[0])} letras")

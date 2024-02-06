# Exercício 77 - Contando Vogais em Tupla

palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON",
            "CURSO", "GRATIS", "ESTUDAR", "PRATICAR",
            "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")
for p in palavras:
  print(f"\nNa palavra {p} temos ", end="")
  for v in p:
    if v in "AEIOU":
      print(f"{v} ", end="")

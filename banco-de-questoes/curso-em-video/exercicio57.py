# Exercício 57 - Validação de Dados

sexo = input("Informe seu sexo: [M/F] ").strip().lower()
while True:
  if sexo == "m":
    print("Sexo M registrado com sucesso!")
    break
  elif sexo == "f":
    print("Sexo F registrado com sucesso!")
    break
  else:
    sexo = input("Dados inválidos. Por favor, informe seu sexo: [M/F] ").strip().lower()

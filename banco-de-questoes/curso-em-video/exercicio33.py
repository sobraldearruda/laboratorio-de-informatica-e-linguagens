# Exercício 33 - Maior e Menor Valores

primeiro = float(input("Primeiro valor: "))
segundo = float(input("Segundo valor: "))
terceiro = float(input("Terceiro valor: "))
menor = primeiro
maior = primeiro
if segundo < primeiro and segundo < terceiro:
  menor = segundo
if segundo > primeiro and segundo > terceiro:
  maior = segundo
if terceiro < primeiro and terceiro < segundo:
  menor = terceiro
if terceiro > primeiro and terceiro > segundo:
  maior = terceiro
print(f"O menor valor digitado foi {menor:.2f}")
print(f"O maior valor digitado foi {maior:.2f}")

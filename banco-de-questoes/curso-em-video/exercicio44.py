# Exercício 44 - Gerenciador de Pagamentos

print("=" *12, "LOJAS SOBRAL", "=" * 12)
compras = float(input("Preço das compras: R$"))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opçao = int(input("Qual é a opção? "))
if opçao == 1:
  desconto = (compras * 10) / 100
  print(f"Sua compra de R${compras:.2f} vai custar {compras - desconto:.2f} no final.")
elif opçao == 2:
  desconto = (compras * 5) / 100
  print(f"Sua compra de R${compras:.2f} vai custar {compras - desconto:.2f} no final.")
elif opçao == 3:
  print(f"Sua compra de R${compras:.2f} vai custar {compras:.2f} no final.")
elif opçao == 4:
  parcelas = int(input("Quantas parcelas? "))
  juros = (compras * 20) / 100
  print(f"Sua compra será parcelada em {parcelas}x de {(compras + juros) / parcelas} com juros.")
  print(f"Sua compra de R${compras:.2f} vai custar {compras + juros:.2f} no final.")

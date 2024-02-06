# Exercício 43 - Índice de Massa Corporal

peso = float(input("Qual é seu peso? (kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.1f}")
if imc < 18.5:
  print("Você está abaixo do peso normal.")
elif imc >= 18.5 and imc < 25:
  print("Parabéns, você está na faixa de peso normal.")
elif imc >= 25 and imc < 30:
  print("Você está em sobrepeso.")
elif imc >= 30 and imc < 40:
  print("Você está em obesidade.")
else:
  print("Você está em obesidade mórbida, cuidado.")

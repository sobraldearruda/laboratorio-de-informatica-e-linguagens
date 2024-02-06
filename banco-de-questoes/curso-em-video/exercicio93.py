# Exercício 93 - Cadastro de Jogador de Futebol

dic = {}
gols = []
dic["nome"] = input("Nome do Jogador: ")
partidas = int(input(f"Quantas partidas {dic['nome']} jogou? "))
for i in range(0, partidas):
  gols.append(int(input(f"Quantos gols na partida {i+1}? ")))
print("-=" * 20)
dic["gols"] = gols
dic["total"] = sum(gols)
print(dic)
print("-=" * 20)
for k, v in dic.items():
  print(f"O campo {k} tem o valor {v}.")
print("-=" * 20)
print(f"O jogador {dic['nome']} jogou {partidas} partidas.")
for i, v in enumerate(dic["gols"]):
  print(f" => Na partida {i+1}, fez {v} gols.")
print(f"Foi um total de {dic['total']} gols.")

# Exercício 86 - Matriz em Python

zero = []
um = []
dois = []
for z in range(0, 3):
  zero.append(int(input(f"Digite um valor para [0, {z}]: ")))
for u in range(0, 3):
  um.append(int(input(f"Digite um valor para [1, {u}]: ")))
for d in range(0, 3):
  dois.append(int(input(f"Digite um valor para [2, {d}]: ")))
print("=" * 30)
print(f"[{zero[0]:^5}] [{zero[1]:^5}] [{zero[2]:^5}]")
print(f"[{um[0]:^5}] [{um[1]:^5}] [{um[2]:^5}]")
print(f"[{dois[0]:^5}] [{dois[1]:^5}] [{dois[2]:^5}]")

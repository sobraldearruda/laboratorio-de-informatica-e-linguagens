## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Concatena Simétricos

def concatena_simetricos(valores):
  lista = []
  if len(valores) % 2 == 0:
      for e in range(0, len(valores)-1):
        um = valores[e]
        dois = valores[-e-1]
        palavra = valores[e] + valores[-e-1]
        if um > dois:
          lista.append(valores[-e-1] + valores[e])
        elif um < dois:
          lista.append(valores[e] + valores[-e-1])
        else:
          lista.append(valores[e] + valores[-e-1])
      lista.pop(-1)
      return lista
  else:
    contador = -1
    cond = ( len(valores) - 1 ) / 2
    for e in range(0, len(valores)-1):
      contador += 1
      if contador != cond:
        um = valores[e]
        dois = valores[-e-1]
        palavra = valores[e] + valores[-e-1]
        if um > dois:
          lista.append(valores[-e-1] + valores[e])
        elif um < dois:
          lista.append(valores[e] + valores[-e-1])
        else:
          lista.append(valores[e] + valores[-e-1])
        lista.append(palavra)
      else:
        lista.append(valores[e])
        break
    lista.pop(-1)
  return lista
x = ["bola", "tv", "zebra", "arara"]
y = ["ab", "cd", "ef", "gh", "ij"]
u = ["cd", "gh", "ck"]
print(concatena_simetricos(u))

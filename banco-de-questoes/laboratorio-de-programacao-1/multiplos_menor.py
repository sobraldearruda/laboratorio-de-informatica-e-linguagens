## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Múltiplos do menor

def menor(lista):
    menor = []
    for i in range(len(lista)):
        if i == 0:
            menor = lista[i]
        else:
            if lista[i] < menor:
                menor = lista[i]
    return menor
def remove_multiplos_do_menor(lista):
    menor = menor(lista)
    for i in range(len(lista) -1, -1, -1):
        if lista[i] % menor == 0:
            lista.pop(i)
    return None
l1 = [6, 9, 10, 3, 5]
l2 = [10, 20, 5, 24, 31]
print(remove_multiplos_do_menor(l1))
print(remove_multiplos_do_menor(l2))

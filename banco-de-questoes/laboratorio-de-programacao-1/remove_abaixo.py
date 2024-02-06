## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Remove abaixo da média

def remove_abaixo_media(lista):
    if len(lista) > 0:
        media = 0
        for num in lista:
            media += num
        media = media / len(lista)
        i = len(lista) - 1
        while not i == -1:
            if lista[i] < media:
                lista.pop(i)
                i = len(lista)
            i-=1

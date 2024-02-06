## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Afinidade musical

def tem_afinidade(l1, l2):
    count = 0
    for l in range(len(l1)):
        for i in range(len(l2)):
            if l1[l] == l2[i]:
                count += 1
    if count >= 3:
        return(True)
    else:
        return(False)

## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Inverte 2 a 2

def inverte2a2_condicional(seq):
    new = []
    for s in range(len(seq) -1):
        if s % 2 == 0:
            if seq[s] > seq[s+1]:
                new.append(seq[s+1])
                new.append(seq[s])
            else:
                new.append(seq[s])
                new.append(seq[s+1])
    if len(seq) % 2 != 0:
        new.append(seq[len(seq)-1])
    for n in new:
        seq.pop(0)
        seq.append(n)
seq = [3, 1, 2, 3, 10, 5, 6]
inverte2a2_condicional(seq)
print(seq)
assert seq == [1, 3, 2, 3, 5, 10, 6]

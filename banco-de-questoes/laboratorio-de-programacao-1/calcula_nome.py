## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Calcula Nome

name = input('Nome? ')
letter = float(input('Letra? R$ '))
length = len(name)
budget = length * letter
print('Orçamento: R$ {:.1f}'.format(budget))

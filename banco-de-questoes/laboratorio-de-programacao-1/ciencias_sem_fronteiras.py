## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Ciências sem Fronteiras

enem = float(input())
credits = float(input())
if enem < 600 and (credits < 83.2 or credits > 374.4):
    print("Nenhuma condição satisfeita.")
elif enem < 600:
    print("Condição ENEM não satisfeita.")
elif enem >= 600 and (credits < 83.2 or credits > 374.4):
    print("Condição CRÉDITOS não satisfeita.")
elif enem >= 600 and (credits >= 83.2 or credits <= 374.4):
    print("Todas as condições satisfeitas.")

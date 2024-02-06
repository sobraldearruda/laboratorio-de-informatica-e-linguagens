## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Orçamento Construção

bricks_price = float(input("Digite o preço da unidade do tijolo (Em reais): "))
bricks_height = float(input("Digite a altura do tijolo (Em metros): "))
bricks_length = float(input("Digite o comprimento do tijolo (Em metros): "))
walls_height = float(input("Digite a altura das paredes (Em metros): "))
walls_length = float(input("Digite o comprimento das paredes (Em metros): "))
bricks_area = bricks_height * bricks_length
walls_area = walls_height * walls_length
bricks_amount = walls_area / bricks_area
budget = bricks_amount * bricks_price
print(f"O número total de tijolos é {bricks_amount:.1f} e o orçamento final é de R$ {budget:.1f}")

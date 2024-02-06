## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Resumo passagem

identifier = input()
schedule = input()
seat = input()
gate = input()
no_tax = float(input())
total_price = float(input())
tax_percent = ((total_price - no_tax) * 100) / total_price
print("### Cartão de Embarque ###")
print(f"Identificador do voo: {identifier}")
print(f"Horário: {schedule}")
print(f"Assento: {seat}")
print(f"Portão: {gate}")
print(f"Total de Imposto: {tax_percent:.1f}%")

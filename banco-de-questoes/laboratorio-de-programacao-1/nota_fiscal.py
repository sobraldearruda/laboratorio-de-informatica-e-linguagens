## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Imprime Nota Fiscal

total = float(input())
date = input()
products = int(input())
average = total / products
print(f"Data: {date}")
print(f"O valor total da compra foi de R$ {total:.2f}. 
      A média do preço dos produtos é de {average:.1f}.")

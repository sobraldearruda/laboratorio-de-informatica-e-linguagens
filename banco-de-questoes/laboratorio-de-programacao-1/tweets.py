## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Tweets por página

tweets = int(input())
pages = tweets // 400
rest = tweets % 400
percentage = (rest * 100) / tweets
print(f"Serão necessárias {pages} página(s) para visualizar os tweets.")
print(f"{percentage:.1f}% dos tweets serão perdidos.")

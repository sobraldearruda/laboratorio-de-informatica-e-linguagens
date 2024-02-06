# Exercício 73 - Tuplas com Times de Futebol

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')
print("=-" * 50)
print(f"Lista de times do Brasileirão: {times}")
print("=-" * 50)
print(f"Os 5 primeiros são {times[:5]}")
print("=-" * 50)
print(f"Os 4 últimos são {times[16:]}")
print("=-" * 50)
print(f"Time em ordem alfabética: {sorted(times)}")
print("=-" * 50)
print(f"O Chapecoense está na {times.index('Chapecoense')+1}ª posição")

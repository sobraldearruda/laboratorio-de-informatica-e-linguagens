## UFCG
## Ciência da Computação
## Programação I / Laboratório de Programação I
## Rafael de Arruda Sobral
## Movimento uniformemente variado

initial_position = float(input("Posição inicial? "))
initial_speed = float(input("Velocidade inicial? "))
time = float(input("Tempo? "))
acceleration = float(input("Aceleração? "))
final_speed = initial_speed + (acceleration * time)
average_speed = initial_speed + ((acceleration * time) / 2)
final_position = (initial_position + (initial_speed * time)) + ((acceleration * time ** 2) / 2)
print("\nDados da questão\n================")
print(f"   Posição inicial: {initial_position:.2f} m")
print(f"Velocidade inicial: {initial_speed:.2f} m/s")
print(f"        Aceleração: {acceleration:.2f} m/s2")
print(f"             Tempo: {time:.2f} s")
print(f"  Velocidade final: {final_speed:.2f} m/s")
print(f"  Velocidade média: {average_speed:.2f} m/s")
print(f"     Posição final: {final_position:.2f} m")

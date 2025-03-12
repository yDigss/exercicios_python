from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "pensar" em um número entre 0 e 5
print('-=-'*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-'*20)
jogador = int(input("Em que número eu pensei? ")) # Jogador tenta adivinhar

print("Processando...")
sleep (2)

if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print(f"Você perdeu eu pensei no número {computador} e não no número {jogador}")
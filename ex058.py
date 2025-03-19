from random import randint
from time import sleep

computador = randint(0, 100) # Faz o computador "pensar" em um número entre 0 e 100
print('-=-'*20)
print("Vou pensar em um número entre 0 e 100. Tente adivinhar...")
print('-=-'*20)
jogador = int(input("Em que número eu pensei? ")) # Jogador tenta adivinhar

print("Processando...")
sleep (1)

palpites = 0

while jogador != computador:
    print("Você errou, tente novamente!")
    if jogador < computador:
        print("mais...")
    else:
        print("menos...")
    palpites += 1
    jogador = int(input("Em que número eu pensei? "))
    print("Processando...")
    sleep (1)

if jogador == computador:
    print(f"Você acertou! eu pensei no numero {computador}, foram necessarias {palpites} tentativas para acertar")
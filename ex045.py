from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Qual é sua escolha? "))

print("JO")
sleep(0.7)
print("KEN")
sleep(0.7)
print("PO!!!")

print('-='*11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print('-='*11)

if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE!")

    elif jogador == 1:
        print("jogador VENCE!")

    elif jogador == 2:
        print("Jogador VENCE!")
    
    else:
        print("Jogada INVÁLIDA!")

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print("Computador VENCE!")
    elif jogador == 1:
        print("EMPATE!")

    elif jogador == 2:
        print("Jogador VENCE!")

    else:
        print("Jogada INVÁLIDA!")

elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print("Jogador VENCE!")

    elif jogador == 1:
        print("Computador VENCE!")

    elif jogador == 2:
        print("EMPATE!")

    else:
        print("Jogada inválida!")





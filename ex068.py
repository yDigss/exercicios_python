from random import randint

v = 0

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Impar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. O total foi {total}")
    
    if tipo == "P":
        if total % 2 == 0:
            print("Você Venceu!")
            v += 1
        else:
            print("Você Perdeu!")
            break

    elif tipo == "I":
        if total % 2 == 1:
            print("Você Venceu!")
            v += 1
        else:
            print("Você Perdeu!")
            break
    print("Vamos jogar novamente...")
    
print(f"Game over você venceu {v} vezes.")
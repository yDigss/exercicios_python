listagem = ("Lápis", 1.75,
            "Borracha", 2,
            "Caderno", 15.90,
            "Estojo", 25,
            "Mochila", 120.32,
            "Caneta", 22,
            "Livro", 34.90)
print("-="*30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-="*30)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end=" ")
    else:
        print(f"R${listagem[pos]:>7.2f}")
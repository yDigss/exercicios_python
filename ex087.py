matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_coluna3 = 0

for l in range(3):
    for c in range(3):
        matriz [l] [c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if matriz [l] [c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_coluna3 += matriz[l][c]

maior_valor_linha2 = max(matriz[1])

print("-="*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz [l] [c]:^5}]', end='')
    print()
print(f"A soma dos números pares é {soma_pares}")
print(f"A soma dos valores da terceita coluna é {soma_coluna3}")
print(f"O maior valor da segunda linha é {maior_valor_linha2}")
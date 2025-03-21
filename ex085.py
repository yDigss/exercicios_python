lista_numeros = [[], []]

for i in range (7):
    
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        lista_numeros[0].append(num)
    else:
        lista_numeros[1].append(num)

print(f"Os valores PARES digitados foram {sorted(lista_numeros[0])}")
print(f"Os valores IMPARES digitados foram {sorted(lista_numeros[1])}")
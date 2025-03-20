valor = []

while True:
    num = int(input("Digite um número: "))
    if num in valor:
        print("O número ja foi adicionado...")
    else:
        valor.append(num)
    resp = str(input("Quer continuar? [S/N]")).strip().upper()
    if resp == 'S':
        continue
    else:
        break
print(f"Você digitou os valores {sorted(valor)}")
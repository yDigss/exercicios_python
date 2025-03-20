valor = []
cont = 0

while True:
    num = int(input("Digite um número: "))
    if num in valor:
        print("O número ja foi adicionado...")
    else:
        valor.append(num)
        cont += 1
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if resp == 'S':
        continue
    else:
        break
print(f"Você digitou {cont} elementos")
print(f"Os valores em ordem decrescente são {sorted(valor, reverse=True)}")
if 5 in valor:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não faz parte da lista!")
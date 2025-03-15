soma = 0
cont = 0
for i in range(1, 7):
    n = int(input(f"Digite {i}° valor: "))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f"Você informou {cont} números PARES e a soma entre eles foi {soma}.")
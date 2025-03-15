num = int(input("Digite um valor: "))
tot = 0
for i in range (1, num+1):
    if num % i == 0:
        print('\033[31m', end =' ')
        tot += 1
    else:
        print('\033[34m', end = ' ')
    print(f"{i}", end =' ')
print(f"\033[m o Número {num} foi divisivel {tot} vezes")
if tot == 2:
    print("E por isso ele É um número PRIMO")
else:
    print("E por isso ele NÃO é um número PRIMO")
#Desafio 10 usei o while para ser mais eficaz mesmo sendo um metodo mais avançado resolvi com ajuda de ia

num1 = int(input('Forneça um número para ver sua tabuada: '))
cont = 1
while cont <= 10:
    print(f'{num1}x{cont}={num1*cont} ')
    cont = cont + 1
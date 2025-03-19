n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:

    print("""
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair""")

    opcao = int(input("Qual sua opção? "))

    if opcao == 1:
        soma = n1 + n2
        print(f"A soma entre {n1} e {n2} é {soma}")

    elif opcao == 2:
        multiplicar = n1 * n2
        print(f"A multiplicação de {n1} e {n2} é {multiplicar}")

    elif opcao == 3:
        if n1 > n2:
            print(f"O {n1} é maior que {n2}")

        else:
            print(f"O {n2} é maior que {n1}")

    elif opcao == 4:
        print("Informe os números novamente")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))

    elif opcao == 5:
        break

    else:
        print("Opcao inválida")
    print("-="*10)
print("Fim do programa")
def soma():
    return num1 + num2

def subtrair():
    resultado = num1 - num2

def multiplicar():
    resultado = num1 * num2

def dividir():
    resultado = num1 / num2

while True:
    print ("Olá, bem vindo!")

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print("1 - Soma")
    print("2 - Subtrair")
    print("3 - multiplicar")
    print("4 - Dividir")
    print("5 - sair")

    escolha = int(input("Escolha a opção de calculo: "))

    if escolha == 1:
        print(soma)

    elif escolha == 2:
        print(subtrair)

    elif escolha == 3:
        print(multiplicar)

    elif escolha == 4:
        print(dividir)

    elif escolha == 5:
        print("Obrigado por usar o programa!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")



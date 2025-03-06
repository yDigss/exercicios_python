saldo = 1000  # Saldo inicial

def sacar(valor):
    global saldo
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > 1000:
        print("Você não pode sacar mais de R$ 1000,00 de uma vez.")
    else:
        saldo -= valor
        print(f"Saque realizado com sucesso! Foram retirados R$ {valor} e agora seu saldo é de R$ {saldo}")


while True:
    print("Olá, bem-vindo(a) ao nosso banco! O que você deseja realizar?")
    print("1 - Saque")
    print("2 - Depósito")
    print("3 - Saldo")
    print("4 - Sair")

    entrada = int(input("Digite o número aqui: "))

    if entrada == 1:
        valor_saque = int(input("Informe quanto você deseja sacar: R$ "))
        sacar(valor_saque)

    elif entrada == 2:
        valor_deposito = int(input("Informe o valor do depósito: R$ "))
        saldo += valor_deposito
        print(f"Depósito de R$ {valor_deposito} realizado com sucesso! Seu saldo agora é de R$ {saldo}")

    elif entrada == 3:
        print(f"Seu saldo atual é de R$ {saldo}")

    elif entrada == 4:
        print("Obrigado por usar nosso banco! Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input ("Informe o valor do deposito: "))
        if valor >0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Deposito realizado com sucesso!")
        else:
            print("Valor invalido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você excedeu seu limite de saldo.")

        elif excedeu_limite:
            print("Operação falhou! Você excedeu seu limite de saque.")

        elif excedeu_saques:
            print("operação falhou! número maximo de saques atingido.")    

        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso! Seu saldo agora é R$ {saldo:.2f}") 

        else:
            print("Operação falhou! Valor informado incorreto.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao =="q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")    
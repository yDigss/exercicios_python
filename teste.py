class ContaBancaria:
    def __init__(self, titular):
        # Inicialize a conta bancária com o nome do titular, saldo 0 e uma lista para armazenar as operações realizadas
        self.titular = titular
        self.saldo = 0
        self.operacoes = []  # Lista para armazenar as operações realizadas

    def depositar(self, valor):
        # Realiza um depósito e registra a operação
        self.saldo += valor
        self.operacoes.append(f"+{valor}")  # Adiciona a operação ao extrato

    def sacar(self, valor):
        # Realiza um saque, se houver saldo suficiente
        if valor > self.saldo:
            print("Saque não permitido")  # Registra a operação de saque não permitido
        else:
            self.saldo -= valor
            self.operacoes.append(f"{-valor}")  # Registra a operação negativa (saque)

    def saldo_atual(self):
        # Retorna o saldo atual
        return self.saldo

    def extrato(self):
        # Exibe o extrato da conta com as operações realizadas e o saldo final
        operacoes_str = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_str}; Saldo: {self.saldo}")


# Leitura do nome do titular
nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

# Leitura das transações (valores de depósito e saque)
entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Processa cada transação
for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

# Exibe o extrato final
conta.extrato()

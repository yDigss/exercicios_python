def leiaInt(prompt):
    """
    Função para ler um número inteiro com validação.

    Parâmetro:
    prompt (str): Mensagem que será exibida ao usuário para solicitar a entrada.

    Retorna:
    int: O valor numérico digitado pelo usuário.
    """
    while True:
        try:
            valor = int(input(prompt))  # Tenta converter a entrada para inteiro
            return valor
        except ValueError:
            print("Erro! Por favor, digite um número inteiro válido.")  # Mensagem de erro

# Programa principal
n = leiaInt("Digite um número: ")
print(f"Você digitou o número: {n}")


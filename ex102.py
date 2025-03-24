def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.

    Parâmetros:
    n (int): O número a ser calculado.
    show (bool, opcional): Se True, mostra o processo de cálculo. Padrão é False.

    Retorna:
    int: O resultado do fatorial de n.
    """
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
        if show:
            print(f"{i} {'x' if i > 1 else '='} ", end="")
    
    if show:
        print(resultado)  # Mostra o resultado final
    
    return resultado


# Exemplos de uso
print(fatorial(5))       # Apenas o resultado
print(fatorial(5, True)) # Mostra o processo passo a passo

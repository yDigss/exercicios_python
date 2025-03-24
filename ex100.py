from random import randint

lista_numeros = []

def sortear():
    numeros = [randint(1, 100) for _ in range(5)]
    lista_numeros.extend(numeros)
    return numeros

def soma_par():
    return sum(num for num in lista_numeros if num % 2 == 0)  # Soma apenas os números pares

# Chamando a função para sortear números
print(f"Números sorteados: {sortear()}")

# Verificando o tamanho da lista
print(f"Tamanho da lista: {len(lista_numeros)}")

# Calculando a soma dos números pares
print(f"Soma dos números pares: {soma_par()}")

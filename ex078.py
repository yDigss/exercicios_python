valores = []

for i in range(5):
    valor = int(input(f"Digite um valor para a posição {i+1}: "))
    valores.append(valor)

maior = max(valores)
menor = min(valores)

posicoes_maior = [i + 1 for i, v in enumerate(valores) if v == maior]
posicoes_menor = [i + 1 for i, v in enumerate(valores) if v == menor]

print(f"\nValores digitados: {valores}")
print(f"Maior valor digitado: {maior}, nas posições {posicoes_maior}")
print(f"Menor valor digitado: {menor}, nas posições {posicoes_menor}")
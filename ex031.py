distancia = int(input("Digite a distância total a viagem: "))
print(f"Você está prestes a iniciar uma viagem de {distancia} Km.")

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"O preço de sua passagem será de R${preco:.2f}.")
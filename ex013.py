#Desafio13
preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100) 

print(f'O produto que custava R$ {preco:.2f} agora custa R${novo:.2f}')
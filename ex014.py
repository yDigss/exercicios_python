salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print(f'O novo salário do funcionário é R${novo:.2f}')
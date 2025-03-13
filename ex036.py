casa = float(input("Valor da casa? R$ "))
salario = float(input("Qual é o seu salário? R$ "))
anos = int(input("Quantos anos de financiamento? "))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f"Para pagar uma casa de RS${casa} em {anos} anos terá uma prestação de R${prestacao:.2f} ")

if prestacao <= minimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!")
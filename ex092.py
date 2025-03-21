from datetime import datetime

dados = dict()

dados['nome'] = str(input("Nome: ")).capitalize()
nascimento = int(input("Ano de nascimento: "))
dados['idade'] = datetime.now().year - nascimento
dados['CPTS'] = int(input("Carteira de Trabalho (0 não tem): "))

if dados['CPTS'] != 0:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: R$"))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)

for k, v in dados.items():
    print(f" - {k.capitalize()} tem o valor {v}")
aluno = {}
aluno['Nome'] = str(input("Nome: ")).capitalize()
aluno['Média'] = float(input(f"Média de {aluno['Nome']}: "))

if aluno['Média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5<= aluno['Média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-='*10)

for k, v in aluno.items():
    print(f"{k} é igual a {v}")

pessoas = []
soma_idade = 0

while True:
    pessoa = {}
    pessoa['nome'] = input("Nome: ").strip().capitalize()
    
    while True:
        pessoa['sexo'] = input("Sexo [M/F]: ").strip().upper()
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Digite apenas M ou F.")
    
    pessoa['idade'] = int(input("Idade: "))
    soma_idade += pessoa['idade']
    pessoas.append(pessoa)
    
    resp = input("Quer continuar? [S/N] ").strip().upper()
    if resp == 'N':
        break

# Cálculo da média de idade
media_idade = soma_idade / len(pessoas)

# Lista de mulheres
mulheres = [p['nome'] for p in pessoas if p['sexo'] == 'F']

# Lista de pessoas acima da média de idade
acima_da_media = [p for p in pessoas if p['idade'] > media_idade]

print("-=" * 30)
print(f"A) Foram cadastradas {len(pessoas)} pessoas.")
print(f"B) A média de idade é {media_idade:.2f} anos.")
print(f"C) As mulheres cadastradas foram: {', '.join(mulheres) if mulheres else 'Nenhuma'}")
print("D) Lista de pessoas com idade acima da média:")
for p in acima_da_media:
    print(f"   → {p['nome']} com {p['idade']} anos")

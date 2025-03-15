somaidade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = 0
totmulher20 = 0

for p in range (1, 5):
    print(f"----- {p}° PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input(" Sexo [M/F]: ")).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm' :
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media_idade = somaidade / 4
print(f"A média de idade do grupo é de {media_idade} anos.")
print(f"O homem mais velho tem {maior_idade_homem} anos e se chama {nome}")
print(f"Existem {totmulher20} mulheres com menos de 20 anos")
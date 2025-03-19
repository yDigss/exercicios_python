total_18 = 0
total_homem = 0
total_mulher_20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]

    if idade >= 18:
        total_18 += 1
    if sexo == "M":
        total_homem += 1
    if sexo == "F" and idade < 20:
        total_mulher_20 += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {total_18}")
print(f"Ao todo temos o total de {total_homem} cadastrados")
print(f"E temos {total_mulher_20} mulheres com menos de 20 anos")
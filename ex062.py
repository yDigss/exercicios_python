primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f"{termo}", end =" -> ")
        termo += razao
        contador += 1

    print("Pausa")
    mais = int(input("Quantos termos você quer a mais? "))
print(f"Progressao finalizada com o total de {total} termos")
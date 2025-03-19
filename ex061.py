primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
termo = primeiro
contador = 1

while contador <= 10:
    print(f"{termo}", end =" -> ")
    termo += razao
    contador += 1

print("ACABOU")
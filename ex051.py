primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Razão: "))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo, razao):
    print(f"{i}", end=' → ')
print("ACABOU")
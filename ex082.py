lista_total = []
lista_par = []
lista_impar = []

while True:
    num = int(input("Digite um número: "))
    lista_total.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    resp = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if resp == 'S':
        continue
    else:
        break
    
print("\nListas geradas:")
print(f"📌 Lista completa: {lista_total}")
print(f"🔹 Números pares: {lista_par}" if lista_par else "⚠️ Nenhum número par foi digitado.")
print(f"🔸 Números ímpares: {lista_impar}" if lista_impar else "⚠️ Nenhum número ímpar foi digitado.")

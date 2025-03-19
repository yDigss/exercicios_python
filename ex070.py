total = totmil = 0
barato = ''
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("{:-^40}".format("Fim do programa"))
print(f"Total gasto: R${total:.2f}")
print(f"Total de produtos acima de R$1000.00: {totmil}")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")
print('-=' * 8, 'LOJAS GUANABARA', '-=' * 8)

preco = float(input("Preço das compras: "))

print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    desconto = preco - (preco * 10/100)
elif opcao == 2:
    desconto = preco - (preco * 5/100)
elif opcao == 3:
    desconto = preco
    parcela = desconto / 2
    print(f"Sua compra será parcelada em 2x de R${parcela}")
elif opcao == 4:
    desconto = preco - (preco * 20/100)
    totalparc = int(input("Quantas parcelas: "))
    parcela = desconto / totalparc
    print(f"Sua compra será parcelada em {totalparc}x de R${parcela}")

print(f"Sua compra de R${preco:.2f} vai custar {desconto}")
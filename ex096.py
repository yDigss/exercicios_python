def area(larg, compri):
    a = larg * compri
    print(f"A area de um terreno {larg}x{compri} é de {a} m2.")


print("Controle de Terreno")
print('-'*20)

largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area(largura, comprimento)
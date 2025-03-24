def maior_valor(qntd):
    numeros = []
    for i in range (qntd):
        num = int(input(f"Informe o {i+1}° número: "))
        numeros.append(num)
    return max(numeros)


quantidade = int(input("Quantos números deseja informar? "))
print(f"O maior valor informado foi: {maior_valor(quantidade)}")
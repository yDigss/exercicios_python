#Simples, composto, encadeado

n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

#calcular a media aritmetica das notas

media = (n1 + n2) /2

if media >= 7:
    print("resultado: Aprovado!")
    print("Parabéns")

elif media >=5:
    print("resultado: Recuperação!")
    
else:
    print("resultado: Reprovado...")

print(f'Sua média é {media}')
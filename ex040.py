nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) /2

if media >= 7:
    print(f"Você foi APROVADO com uma média de {media:.1f}.")
elif media > 5:
    print(f"Você está de RECUPERAÇÃO com uma média de {media:.1f}.")
else:
    print(f"Você está REPROVADO tendo uma média de {media:.1f}")
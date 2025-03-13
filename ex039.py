from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print(f"Quem nasceu em {nascimento} tem {idade} anos em {atual}")

if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!")
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print(f"Você já deveria estar alistado há {saldo} anos")
    print(f"Seu alistamento foi em {ano}")
else:
    saldo = 18 - idade
    ano = atual + saldo
    print(f"Ainda faltam {saldo} anos para o alistamento.")
    print(f"Seu alistamento será em {ano}")
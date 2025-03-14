from datetime import date

ano_nascimento = int(input("Em que ano você nasceu? "))
atual = date.today().year
idade = atual - ano_nascimento
print(f"O atleta tem {idade} anos.")

if idade <= 9:
    print(f"Nadador Mirim")
elif idade <=14:
    print(f"Nadador Infantil")
elif idade <=19:
    print(f"Nadador Jûnior.")
elif idade <=25:
    print(f"Nadador Sênior")
else:
    print(f"Nadador Master")
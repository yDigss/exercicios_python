sexo = input("Digite o seu sexo (M/F): ").strip().upper()

while sexo not in ("M", "F"):
    print("Erro! Por favor, digite apenas M para masculino ou F para feminino.")
    sexo = input("Digite o seu sexo novamente (M/F): ").strip().upper()
if sexo == "M":
    print("Seu sexo é masculino.")
else:
    print("Seu sexo é feminino")
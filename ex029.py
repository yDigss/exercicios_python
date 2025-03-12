velocidade = int(input("Qual a velocidade do carro? "))

if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido de 80Km/h.")
    multa = (velocidade - 80) * 7
    print(f"Você deve pagar uma multa de: {multa}")
print("Tenha um bom dia! dirija com segurança!")
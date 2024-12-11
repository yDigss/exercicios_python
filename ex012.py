altura = float(input('Qual é a altura da sua parede?: '))
largura = float(input('Qual é a largura da sua parede?: '))
# Calcula a área da parede
area = altura * largura
litros_tinta = area / 2

print(f'A área da sua parede é de {area:.2f}m2')
print(f'Você precida de {litros_tinta:.2f}L para pintar a sua parede')

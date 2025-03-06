from imc import calcula_imc
from imc import classifica_imc

print("Inicio do programa")
indice = calcula_imc(altura=1.80, peso=70)
print("IMC:", indice)
classificacao_imc = classifica_imc(indice)
print(classificacao_imc)
print("Término do programa")
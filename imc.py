print("Módulo IMC importado")

def calcula_imc(peso, altura):
    print("Parametro peso:", peso)
    print("Parametro altura:", altura)
    imc = float (peso) / float (altura)**2
    return imc

def classifica_imc(indice):
    if indice < 18.5:
        return 'Baixo peso'
    elif indice < 25:
        return 'Peso normal'
    elif indice < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

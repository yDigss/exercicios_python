def notas(*notas, situacao=False):
    """
    Função que recebe várias notas de alunos e retorna um dicionário com informações.

    Parâmetros:
    *notas (float): As notas dos alunos (quantidade variável).
    situacao (bool, opcional): Se True, inclui a situação (aprovado/reprovado).

    Retorna:
    dict: Dicionário com as informações sobre as notas.
    """
    # Calculando as informações necessárias
    total_notas = len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / total_notas
    situacao_aluno = ''
    
    if situacao:
        if media >= 7:
            situacao_aluno = 'Aprovado'
        elif media >= 5:
            situacao_aluno = 'Recuperação'
        else:
            situacao_aluno = 'Reprovado'
    
    # Criando o dicionário com as informações
    resultado = {
        'Total de notas': total_notas,
        'Maior nota': maior_nota,
        'Menor nota': menor_nota,
        'Média': media
    }
    
    if situacao:
        resultado['Situação'] = situacao_aluno
    
    return resultado

# Exemplo de uso
resultado = notas(5, 6, 7, 8, 10, situacao=True)
print(resultado)

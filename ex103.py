def ficha(jogador="<desconhecido>", gols=0):
    """
    Exibe a ficha de um jogador de futebol.

    Parâmetros:
    jogador (str, opcional): Nome do jogador. Padrão é "<desconhecido>".
    gols (int, opcional): Quantidade de gols marcados. Padrão é 0.

    Retorna:
    str: Ficha do jogador formatada.
    """
    return f"O jogador {jogador} fez {gols} gol(s) no campeonato."


# Programa principal
nome = input("Nome do jogador: ").strip()
gols = input("Número de gols: ").strip()

# Verifica se o nome foi digitado
if nome == "":
    nome = "<desconhecido>"

# Verifica se os gols são um número válido
if gols.isdigit():
    gols = int(gols)
else:
    gols = 0

print(ficha(nome, gols))


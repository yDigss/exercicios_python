from time import sleep

def ajuda(comando):
    """
    Função que exibe o manual de ajuda interativo com cores.

    Parâmetro:
    comando (str): O comando sobre o qual será exibido o manual.
    """
    print(f"\033[1;36m{'-' * 40}\033[m")
    print(f"\033[1;33mAcessando o manual do comando '{comando}'\033[m")
    print(f"\033[1;36m{'-' * 40}\033[m")
    sleep(1)
    help(comando)
    print(f"\033[1;36m{'-' * 40}\033[m")


def sistema_help():
    """
    Função principal que gerencia o mini-sistema de ajuda interativo.
    O usuário pode digitar comandos e ver o manual, ou digitar 'FIM' para encerrar.
    """
    while True:
        print("\033[1;32mDigite o comando para consultar o manual ou 'FIM' para encerrar:\033[m")
        comando = input("\033[1;34mComando: \033[m").strip()

        if comando.lower() == 'fim':
            print("\033[1;31mPrograma encerrado. Até logo!\033[m")
            break
        else:
            ajuda(comando)

# Chama a função principal para iniciar o programa
sistema_help()

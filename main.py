import os

mensagens = []

nome = input("Nome: ")

while True:

    #limpando o terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("___________________")

    #obtendo o texto
    texto = input("menssagem: ")
    if texto == "fim":
        break

    #adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
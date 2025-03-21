time = []

while True:
    jogador = {}
    jogador['nome'] = input("Nome do jogador: ").strip().capitalize()
    
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    jogador['gols'] = []
    
    for i in range(partidas):
        jogador['gols'].append(int(input(f"   → Gols na partida {i + 1}: ")))
    
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador)

    while True:
        resp = input("Quer continuar? [S/N] ").strip().upper()
        if resp in 'SN':
            break
        print("ERRO! Digite apenas S ou N.")
    
    if resp == 'N':
        break

print("-=" * 30)

# Mostrando o cabeçalho da tabela
print(f"{'Cod':<4}{'Nome':<15}{'Gols':<20}{'Total':<5}")
print("-" * 50)

for i, j in enumerate(time):
    print(f"{i:<4}{j['nome']:<15}{str(j['gols']):<20}{j['total']:<5}")

# Exibindo detalhes individuais
while True:
    print("-" * 50)
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    
    if busca == 999:
        break
    if busca >= len(time):
        print("ERRO! Não existe jogador com esse código.")
    else:
        jogador = time[busca]
        print(f"-- Levantamento do jogador {jogador['nome']}:")
        for i, g in enumerate(jogador['gols']):
            print(f"   No jogo {i + 1} fez {g} gols.")

print("<< VOLTE SEMPRE >>")

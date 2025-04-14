from random import randint

# Gera um número aleatório entre 1 e 6
bot = randint(1, 6)

# Variáveis de controle
escolha = 1
acertos = 0
jogadas = 0

# Loop do jogo
while escolha != 0:
    try:
        escolha = int(input('Digite 0 para sair ou escolha um número entre 1-6: '))
        
        # Verifica se o número está no intervalo válido
        if escolha in [1, 2, 3, 4, 5, 6]:
            jogadas += 1  # Conta a jogada

            if escolha == bot:
                print('Você acertou!')
                acertos += 1
            else:
                print('Você errou!')
        
        elif escolha == 0:
            print('Você saiu do jogo!')
        
        else:
            print('Escolha inválida. O jogo encerrou!')
            break

    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')

# Exibe o resumo das jogadas
print(f'Número de jogadas: {jogadas}')
print(f'Número de acertos: {acertos}')

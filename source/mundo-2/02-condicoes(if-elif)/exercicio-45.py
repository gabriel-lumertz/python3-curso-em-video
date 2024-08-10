# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randrange
from time import sleep

tipo = ('Pedra', 'Papel', 'Tesoura')

print(
    '''
    Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    '''
)

jogador1 = int(input('Qual é a sua jogada? '))

jogador2 = randrange(0, 2)

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-=' * 11)
print('O Computador escolheu {}'.format(tipo[jogador2]))
print('Você escolheu {}'.format(tipo[jogador1]))
print('-=' * 11)

if jogador1 == 0: # Jogou pedra
    if jogador2 == 0:
        print('Empate')
    elif jogador2 == 1:
        print('Computador Venceu')
    elif jogador2 == 2:
        print('Você Venceu')
    else:
        print('Jogada inválida')
if jogador1 == 1: # jogou papel
    if jogador2 == 0:
        print('Você venceu')
    elif jogador2 == 1:
        print('Empate')
    elif jogador2 == 2:
        print('Computador venceu')
    else:
        print('Jogada inválida')
if jogador1 == 2: # jogou tesoura
    if jogador2 == 0:
        print('Computador venceu')
    elif jogador2 == 1:
        print('Você Venceu')
    elif jogador2 == 2:
        print('Empate')
    else:
        print('Jogada inválida')
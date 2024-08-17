# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

def calucularTabuada(numero):
    for i in range(1, 11):
        print(f'{numero} X {i} = {i * numero}')

numero = int(input('Digite um número de 1 a 10: '))

while(0 > numero or numero > 10):
    print('Número inválido \n')
    numero = int(input('Digite um número de 1 a 10: '))
else:
    calucularTabuada(numero)
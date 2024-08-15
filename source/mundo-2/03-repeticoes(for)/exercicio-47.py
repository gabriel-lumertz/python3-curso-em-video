# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


# Solução 1
for i in range(1, 51):
    n = i % 2
    if n == 0:
        print(i, end = ' ')

print('\n')

# Solução 2
for i in range(2, 51, 2):
    print(i, end = ' ')
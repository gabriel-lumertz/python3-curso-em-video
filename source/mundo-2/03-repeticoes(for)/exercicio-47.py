# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for i in range(1, 51):
    n = i % 2
    if n == 0:
        print(i)
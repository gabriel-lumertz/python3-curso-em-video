# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0

for i in range(1, 501, 2):
    if(i % 3 == 0):
        contador += 1
        soma += i


print(f'A soma de todos os {contador} valores é {soma}.')
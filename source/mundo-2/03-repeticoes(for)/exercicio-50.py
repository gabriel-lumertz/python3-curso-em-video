# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

numeros = []
soma = []

for i in range(1, 7):
    numeros = (int(input('Digite um número inteiro: ')))
    if(numeros % 2 == 0):
        soma.append(numeros)

print(f'O valor dos números é: {sum(soma)}.')
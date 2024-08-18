# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

numero = int(input('Digite um valor: '))

razao = int(input('Digite um valor: '))

for i in range(1, 11):
    numero += razao
    print(numero)
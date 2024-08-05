# Escreva um programa que leia dois números inteiros a compare—os, mostrando na tala uma mansagam:

# O primairo valor é maior
# O segundo valor e maior
# Não axista valor maior, os dois são iguais

numero_1 = int(input('Digitite um número inteiro: '))

numero_2 = int(input('Digitite um número inteiro: '))

if numero_1 > numero_2:
    print('O primeiro valor é maior.')
elif numero_1 < numero_2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
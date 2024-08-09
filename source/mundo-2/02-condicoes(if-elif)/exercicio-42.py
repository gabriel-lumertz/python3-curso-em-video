# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo lado: '))
lado3 = float(input('Terceiro lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima PODEM formar um triângulo! ', end='')
    if lado1 == lado2 == lado3:
        print('Equilátero.')
    elif lado1 != lado2 != lado3 != lado1:
        print('Escaleno.')
    else:
        print('Isósceles.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')
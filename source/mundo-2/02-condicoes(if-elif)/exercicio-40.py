# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mansagam no final, de acordo com a média atingida:

# Média abaixo de 5.0 REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('A sua média foi {:.1f}. Você está reprovado.'.format(media))
elif media < 6.9:
    print('A sua média foi {:.1f}. Você está em recuperação.'.format(media))
else:
    print('A sua média foi {:.1f}. Você está aprovado.'.format(media))
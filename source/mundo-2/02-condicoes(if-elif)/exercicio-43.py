# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida

peso = int(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('O IMS dessa pessoa é de {:.1f} \n'.format(imc))
    print('Você está abaixo do peso.')
elif imc <= 25:
    print('O IMS dessa pessoa é de {:.1f} \n'.format(imc), end='')
    print('Você está abaixo no peso ideal.')
elif imc <= 30:
    print('O IMS dessa pessoa é de {:.1f} \n'.format(imc), end='')
    print('Você está com sobrepeso.')
elif imc <= 40:
    print('O IMS dessa pessoa é de {:.1f} \n'.format(imc), end='')
    print('Você está abaixo com obesidade.')
else:
    print('O IMS dessa pessoa é de {:.1f} \n'.format(imc), end='')
    print('Você está abaixo com obesidade mórbida.')
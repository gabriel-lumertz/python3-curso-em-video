# Escrava um programa para aprovar o empréstimo bancário para a compra da uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador a em quantos anos ela vai pagar.

# Calcule o valor da prastação mansal, sabendo qua ela não poda exceder 30% do salário ou então o empréstimo sará nagado.


valor_casa = float(input('Qual o valor da casa: R$? '))
valor_salario = float(input('Qual é o seu salário: R$? '))
tempo_pagamento = int(input('Em quantos anos vai ser pago? '))

valor_prestacao = valor_casa / (tempo_pagamento * 12)
percentual_salario = valor_prestacao / valor_salario

if percentual_salario > 0.3:
    print(f'Empréstimo negado. O percentual de comprometimento, {percentual_salario:.1%}, excede 30% do salário.')
else:
    print(
        f'Empréstimo aprovado. Valor da prestação será de {valor_prestacao:.2f}\n'
        f'E será pago em {tempo_pagamento:.0f} meses'
    )
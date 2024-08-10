# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço normal 

# – 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS GUANABARA '))

print('\n')

preco = float(input('Valor das compras: '))

print('\n')

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro ou cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão ')

print('\n')

opcao = int(input('Qual é a opção? '))

if opcao == 4:
    parcelas = int(input('Quantas parcelas? '))

print('\n')

if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'. format(preco, preco * 0.9))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'. format(preco, preco * 0.95))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(preco / 2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'. format(preco, preco))
elif opcao == 4:
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcelas, preco * 1.2 / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'. format(preco, preco * 1.2))
else:
    print('Opção inválida.')
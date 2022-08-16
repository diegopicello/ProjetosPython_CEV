print(10 * '=', 'LOJAS DIDICO', 10 * '=')
preco = float(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO:')
print('[ 1 ] à vista no dinheiro/cheque;')
print('[ 2 ] à vista no cartão;')
print('[ 3 ] 2x no cartão;')
print('[ 4 ] 3x ou mais no cartão.')
escolha = str(input('Qual será a opção de compra? '))
if escolha == '1':
    precofinal = preco * 0.9
    print('Sua compra de R${:.2f} receberá um desconto de 10%, caindo para R${:.2f}.'.format(preco, precofinal))
elif escolha == '2':
    precofinal = preco * 0.95
    print('Sua compra de R${:.2f} receberá um desconto de 5%, caindo para R${:.2f}.'.format(preco, precofinal))
elif escolha == '3':
    print('O preço final de sua compra será o original de R${}.'.format(preco))
elif escolha == '4':
    parcela = int(input('Quantas parcelas? '))
    if parcela >= 3:
        precofinal = preco * 1.2
        valorparcela = precofinal / parcela
        print('O preço final da compra de R${} em {} vezes será de R${} com parcelas de R${}.'.format(preco, parcela, precofinal, valorparcela))
    else:
        print('Opção inválida! Modalidade de 3 ou mais parcelas!')
else:
    print('Opção inválida! Tente novamente com um dos números disponibilizados acima!')




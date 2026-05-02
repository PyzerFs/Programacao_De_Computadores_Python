preco = float(input('Digite o valor da compra: '))

result1 = preco / 10
resultf = result1 * 9

if preco <= 100:
    print('Sua compra não chegou no preço de desconto')
elif preco > 100:
    print(f'Sua compra recebeu desconto! O valor ficou em {resultf}')

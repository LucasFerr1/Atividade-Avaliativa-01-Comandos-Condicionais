valor_saque = float(input('Digite o valor do saque:'))
cedulas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
print('Quantidade de cédulas e moedas necessárias:')
for valor in cedulas_moedas:
    quantidade = int(valor_saque // valor)
    print("R$ {}: {}".format(valor, quantidade))
    valor_saque -= quantidade * valor
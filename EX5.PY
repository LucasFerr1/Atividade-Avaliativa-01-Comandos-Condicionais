tempo = int(input('Digite seu tempo no estacionamento (minutos): '))

if tempo <= 120:
    print('Valor pago: R$08,00')
elif tempo <= 240:
    print('Valor pago: R$13,00')
elif tempo < 300:
    print('Valor pago: R$16,00')
elif tempo < 360:
    print('Valor pago: R$19,00')
elif tempo < 420:
    print('Valor pago: R$22,00')
elif tempo < 480:
    print('Valor pago: R$25,00')
elif tempo < 540:
    print('Valor pago: R$28,00')
elif tempo < 600:
    print('Valor pago: R$31,00')
elif tempo < 660:
    print('Valor pago: R$34,00')
elif tempo < 720:
    print('Valor pago: R$37,00')
else:
    print('Valor pago: R$30,00')
import sys
numero = int(input('Digite um numero de 4 dígitos: '))
if numero < 0 or numero > 9999:
    print('Número inválido')
    sys.exit()
else:
    digito4 = numero % 10
    numero //= 10
    digito3 = numero % 10
    numero //= 10
    digito2 = numero % 10
    numero //= 10
    digito1 = numero
    print('a soma do valor é', digito1 + digito2 + digito3 + digito4)
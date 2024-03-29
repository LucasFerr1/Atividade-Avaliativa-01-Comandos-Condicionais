import sys

dia_inicial = int(input("Digite o dia inicial: "))
mes_inicial = int(input("Digite o mês inicial: "))
dia_final = int(input("Digite o dia final: "))
mes_final = int(input("Digite o mês final: "))

if mes_inicial > mes_final or (mes_inicial == mes_final and dia_inicial > dia_final):
    print("Data inicial não pode ser maior que data final.")
    sys.exit()

meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Se os meses são iguais, basta subtrair os dias
if mes_inicial == mes_final:
    resultado = dia_final - dia_inicial + 1
else:
    dias_totais_intermediarios = sum(meses[mes_inicial+1:mes_final])
    resultado = meses[mes_inicial] - dia_inicial + 1 + dia_final + dias_totais_intermediarios

print(f'O número de dias restantes é {resultado}')
#14. Escreva um programa que pergunte a quantidade de    pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
custo_diario = 60
custo_km = 0.15
km = float(input('Informe a quantidade de km percorridos:'))
dias = float(input('Informe a quantidade de dias pelos quais o carro foi alugado:'))
def calcula(km:float,dias:float):
    valor_km = km * custo_km
    valor_dias = dias * custo_diario
    valor_total = valor_km + valor_dias
    return valor_total

print('O Total a pagar será de: R$%.2f' % calcula(km,dias))
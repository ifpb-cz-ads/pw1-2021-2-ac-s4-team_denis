#13. Escreva um programa que converta uma temperatura digitada em °C em °F.
# A fórmula para essa conversão é: F = 9 × C ÷ 5 + 32
def converter_celsius_para_fahrenheit(n1):
    fahrenheit= ((9 * n1) / 5) +32
    return fahrenheit

valor_celsius = float(input('Informe o valor em celsius:'))
print('O valor %2.f em Celsius é igual ah:'%valor_celsius,converter_celsius_para_fahrenheit(valor_celsius),'Fahrenheit')

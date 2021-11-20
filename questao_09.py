#9. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos.

Dias_Segundos=86400
Horas_Segundos=3600
Minutos_Segundos=60
dias = float(input("Informe a quantidade de dias: "))
horas = float(input("Informe a quantidade de horas: "))
minutos = float(input("Informe a quantidade de minutos: "))
Segundos = float(input("Informe a quantidade de segundos: "))
resultado = (dias * Dias_Segundos)+(horas * Horas_Segundos)+(minutos * Minutos_Segundos) + Segundos
print(f'O valor total em segundos é:{resultado}')
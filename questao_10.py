#10. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário.
salario = float(input('Informe o valor do salario :'))
porcertagem = float(input('Informe o valor da porcertagem do aumento :'))
aumento = salario *( porcertagem /100)
new_salario = salario + aumento
print('O salario foi aumentado em: R$%.2f'%aumento,'por tanto o novo salario é de: R$%.2f'%new_salario)
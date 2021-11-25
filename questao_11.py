#11. Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar.

preco = float(input('Informe o preço da mercadoria:'))
percentual = float(input('Informe o percentual de desconto:'))
desconto = preco * ( percentual /100)
valor_com_desconto = preco - desconto
print('O valor do desconto foi de: R$%1.f'%desconto,'portanto o novo preço a pagar será R$ %.2f'%valor_com_desconto)

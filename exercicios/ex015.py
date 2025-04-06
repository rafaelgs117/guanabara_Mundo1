#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram percorridos? '))
dias_alugados = int(input('Quantos dias o carro foi alugado? '))

custo_dia = 60 # custo por dia em R$
custo_km_rodado = 0.15 # custo por Km rodado em R$

custo_total = (custo_dia * dias_alugados) + (custo_km_rodado * km) #calculo do total a pagar
print('O carro percoreu {} Km e foi alugado por {} dias, totalizando um aluguel de R${:.2f}'.format(km, dias_alugados, custo_total))
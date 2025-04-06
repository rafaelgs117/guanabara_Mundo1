#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$1,00 = R$5,84

dinheiro = float(input('Digite quanto dinheiro você tem na carteira: R$'))
dolar = 5.84 #valor dolar 06/04/2025
quantidade_dolares = dinheiro / dolar #calculo da quantidade de dolares que a pessoa pode comprar

euro = 6.41 #valor euro 06/04/2025
quantidade_euros = dinheiro / euro #calculo da quantidade de euros que a pessoa pode comprar

print('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheiro, quantidade_dolares))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(dinheiro, quantidade_euros))
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco = float(input('Digite o preço do produto: R$'))
desconto = 0.05 #desconto é 5/100 = 0.05
novo_preco = preco - (preco * desconto) # Calcula o novo preço aplicando o desconto de 5%

print('O preço do produto é R${:.2f} e com desconto de 5% seu preço sera de R${:.2f}'.format(preco, novo_preco))
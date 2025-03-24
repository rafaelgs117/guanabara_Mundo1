#Desafio 05: Antecessor e Sucessor
#faça um programa que leia um numero inteiro
#e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número: '))
print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}'.format(n, n-1, n+1))

#Desaio 06: Dobro, Triplo e Raiz Quadrada
#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('Digite um número: '))
print('O número digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n1, n1*2, n1*3, n1**(1/2)))

#Desafio 07: Média Aritmética
#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

print('A média das notas {} e {} é {}'.format(nota1, nota2, media))

#Desafio 08: Conversor de Medidas
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite um valor em metros: '))
centimetros = metros*100

print('O valor de {} metros é igual a {} centímetros'.format(metros, centimetros))

#Desafio 09
#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

tabuada = int(input('Digite um número para ver a tabuada: '))

print('{} x {:2} = {}'.format(tabuada, 1, tabuada*1)) 
print('{} x {:2} = {}'.format(tabuada, 2, tabuada*2))
print('{} x {:2} = {}'.format(tabuada, 3, tabuada*3))
print('{} x {:2} = {}'.format(tabuada, 4, tabuada*4))
print('{} x {:2} = {}'.format(tabuada, 5, tabuada*5))
print('{} x {:2} = {}'.format(tabuada, 6, tabuada*6))
print('{} x {:2} = {}'.format(tabuada, 7, tabuada*7))
print('{} x {:2} = {}'.format(tabuada, 8, tabuada*8))
print('{} x {:2} = {}'.format(tabuada, 9, tabuada*9))
print('{} x {:2} = {}'.format(tabuada, 10, tabuada*10))


#Desafio 10
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$1,00 = R$3,27

dinheuro = float(input('Digite quanto dinheiro você tem na carteira: R$'))
dolar = dinheuro/3.27

print('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheuro, dolar))

#Desafio 11
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la
#Sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura*altura
tinta = area/2

print('A área da parede é de {}m² e você precisará de {} litros de tinta para pintá-la'.format(area, tinta))

#Desafio 12
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

produto = float(input('Digite o preço do produto: R$'))
desconto = produto*0.05
novopreco = produto-desconto

print('O produto custa R${:.2f} e com 5% de desconto ele passa a custar R${:.2f}'.format(produto, novopreco))

#Desafio 13
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Digite o salário do funcionário: R$'))
aumento = salario*0.15
novosalario = salario+aumento

print('O salário do funcionário é de R${:.2f} e com 15% de aumento ele passa a receber R${:.2f}'.format(salario, novosalario))

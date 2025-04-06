#Desafio 08: Conversor de Medidas
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite um valor em metros: '))
centimetros = metros*100
milimetros = metros*1000

print('O valor de {} metros é igual a {} centímetros e {} milímetros'.format(metros, centimetros, milimetros))
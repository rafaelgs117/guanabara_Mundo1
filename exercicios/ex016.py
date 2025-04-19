#crie um programa que leia um numero Real e mostre na tela a sua porção inteira

from math import trunc #importa apenas a função trunc da biblioteca math
#import math importa a biblioteca math inteira
num = float(input('Digite um número: '))

#trunc retorna a parte inteira do número
print('O numero que voce digitol foi {} e a sua parte inteira é {}'.format(num, trunc(num))) #mostra o número digitado e a parte inteira

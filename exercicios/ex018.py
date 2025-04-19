#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
angulo = float(input('Digite o ângulo: '))

seno = math.sin(math.radians(angulo)) #converte o angulo para radianos
cosseno = math.cos(math.radians(angulo)) #prestar atenção quando colocar a biblioteca de acordo com o que está pedindo
tangente = math.tan(math.radians(angulo))

print('O ângulo de {}º tem o seno de {:.2f}\n'.format(angulo, seno))
print('O ângulo de {}º tem o cosseno de {:.2f}\n'.format(angulo, cosseno))
print('O ângulo de {}º tem a tangente de {:.2f}'.format(angulo, tangente))
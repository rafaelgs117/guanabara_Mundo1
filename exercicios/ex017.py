#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.

import math
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2) #formula da hipotenusa

print("O comprimento da hipotenusa é: {:.2f}".format(hipotenusa))

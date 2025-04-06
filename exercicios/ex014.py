#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (temperatura * 9/5) + 32
celsius = (fahrenheit - 32) * 5/9

print('A temperatura de {:.2f} graus Celsius é igual a {:.2f} graus Fahrenheit'.format(temperatura, fahrenheit))
print('E a temperatura de {:.2f} graus Fahrenheit é igual a {:.2f} graus Celsius'.format(fahrenheit, celsius))


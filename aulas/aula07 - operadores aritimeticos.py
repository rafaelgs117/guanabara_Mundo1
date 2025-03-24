# operadores aritimeticos
# orderm d eprecedencia
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -
'''
print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(5//2)
print(5%2)
'''
#valor = 3*5+4**2 # 3*5 = 15 + 4**2 = 16 = 31
#print(valor)

#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:=^20}!'.format(nome)) # centraliza o nome com 20 caracteres

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d)) #depois do "d"),end = '') # end = ' ' não quebra a linha
print('Divisão inteira {} e potencia {}'.format(di, e))
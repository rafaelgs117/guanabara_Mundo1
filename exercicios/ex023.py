#faça um programa que leia um numero de 0 a 9999 e mostre um dos digitos separados
#exemplo: 1834
#digito da milhar: 1
#digito da centena: 8
#digito da dezena: 3
#digito da unidade: 4

n1 = int(input('Digite um numero de 0 a 9999: '))

print('numero digitado foi{}'.format(n1)) # 1834
print('digite unidade: {}'.format(n1 % 10)) # % 10 = 4
print('digito dezena: {}'.format((n1 // 10) % 10)) # // 10 = 183, % 10 = 3
print('digito centena: {}'.format((n1 // 100) % 10)) # // 100 = 18, % 10 = 8
print('digito milhar: {}'.format(n1 // 1000)) # // 1000 = 1

#outra forma de fazer

num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10 # num // 1 = 1834, % 10 = 4 # unidade 
d = num // 10 % 10 # num // 10 = 183, % 10 = 3 # dezena
c = num // 100 % 10 # num // 100 = 18, % 10 = 8 # centena
m = num // 1000 % 10 # num // 1000 = 1, % 10 = 1 # milhar

print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
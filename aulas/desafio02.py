#DESAFIO 01
#crie um programa que leia dois numeros e leia a soma entre eles

n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o segundo valor:"))
s = n1 + n2 

print("A soma entre {} e {} é {}".format(n1,n2,s))

#DESAFIO 02
#faça um programa que leia algo pelo teclado e mostre na tela
#o seu tipo primitivo e todas as informações possiveis sobre ele

a1 = input("Digite algo:")

print("O tipo primitivo desse valor é:", type(a1)) #verifica o tipo primitivo
print("Só tem espaços?", a1.isspace())  #verifica se é espaço
print("É um número?", a1.isnumeric()) #verifica se é número
print("É alfabético?", a1.isalpha()) #verifica se é alfabético


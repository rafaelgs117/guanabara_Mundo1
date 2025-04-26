#faça um programa que leia o nome completo de uma pessoa e mostre em seguida o 
# primeiro e o ultimo nome separadamente.
#ex:
#primeiro = Alise
#ultimo = Animusphere

nome = str(input('Digite seu nome completo: ')).strip()

nome = nome.split() # separa o nome em uma lista de palavras
primeiro = nome[0] # pega o primeiro elemento da lista
ultimo = nome[-1] # pega o ultimo elemento da lista

print(f'Primeiro nome: {primeiro}')
print(f'Ultimo nome: {ultimo}') 


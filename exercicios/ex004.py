#faça um programa que leia algo pelo teclado e mostre na 
#tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))# mostra o tipo primitivo do valor digitado
print('Só tem espaços? ', a.isspace())# verifica se a string é composta apenas por espaços
print('É um número? ', a.isnumeric())# verifica se a string é um número
print('É alfabético? ', a.isalpha())# alfabético é quando tem letras
print('É alfanumérico? ', a.isalnum())# alfanumérico é quando tem letras e números
print('Está em maiúsculas? ', a.isupper())# verifica se a string está em maiúsculas
print('Está em minúsculas? ', a.islower())# verifica se a string está em minúsculas
print('Está capitalizada? ', a.istitle())# capitalizada primeira letra maiúscula e as outras minúsculas
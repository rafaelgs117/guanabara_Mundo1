#crie um programa que leia o nome completo de uma pessoa e mostre:
# a) O nome com todas as letras maiúsculas;
# b) O nome com todas as letras minúsculas;
# c) Quantas letras ao todo (sem considerar espaços);
# d) Quantas letras tem o primeiro nome.


nome = str(input('Digite seu nome completo: ')).strip() #strip remove os espaços no começo e no final da string

print('seu nome em maiúsculas é: {}'.format(nome.upper())) #a) upper transforma a string em maiúscula
print('seu nome em minúsculas é: {}'.format(nome.lower())) #b) lower transforma a string em minúscula
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #c) len conta o número de letras e count conta o número de espaços
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) #d) find encontra o primeiro espaço e conta as letras até ele
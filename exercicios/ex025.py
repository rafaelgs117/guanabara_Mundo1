#crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome em qualquer lugar

nome = str(input('Digite seu nome completo: ')).strip() #strip remove os espaços no início e no final da string

print('seu nome possui "Silva"? {}'.format('silva' in nome.lower())) #lower transforma a string em minúscula para facilitar a comparação
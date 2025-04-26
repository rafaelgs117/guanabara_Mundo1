#crie um programa que leia o nome de uma cidade e diga se ela começa com o nome 'Santo'

cidade = str(input('Digite o nome da cidade: ')).strip() #strip remove os espaços no início e no final da string

print('A cidade começa com Santo? {}'.format(cidade[:5].upper() == 'SANTO')) #[:5] pega os 5 primeiros caracteres da string e upper transforma em maiúscula para facilitar a comparação





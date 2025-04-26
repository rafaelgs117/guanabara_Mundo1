#faça um programa que leia uma frase pelo teclado e mostre;
# quantas vezes aparece a letra "A";
# em que posição ela aparece a primeira vez; 
# em que posição ela aparece a última vez.

fr = str(input('Digite uma frase: ')).strip().upper() #strip remove os espaços no início e no final da string

print('a letra "A" aparece {} vezes na frase'.format(fr.count('A'))) #count conta quantas vezes a letra "A" aparece 
print('a letra "A" aparece pela primeira vez na posição {}.'.format(fr.find('A')+1)) #find encontra a primeira ocorrência da letra "A" e +1 para contar a partir de 1
print('a letra "A" aparece pela última vez na posição {}.'.format(fr.rfind('A')+1)) #rfind encontra a última ocorrência da letra "A" e +1 para contar a partir de 1
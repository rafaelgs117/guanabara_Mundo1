#Professor quer sortear a ordem de apressentação dos alunos.
#Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

from random import shuffle #shuffle embaralha a lista
#ou apenas import random
aluno1 = str(input('Nome do aluno 1: '))
aluno2 = str(input('Nome do aluno 2: '))
aluno3 = str(input('Nome do aluno 3: '))
aluno4 = str(input('Nome do aluno 4: '))

alunos = [aluno1, aluno2, aluno3, aluno4] #cria uma lista com os alunos
shuffle(alunos) #embaralha a lista de alunos

print('A ordem de apresentação será: ')
print(alunos) #mostra a lista de alunos embaralhada
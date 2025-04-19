#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random #importando a biblioteca random
print('-'*12)  #vai colocar - 12x
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4] #colocando os nomes em uma lista
sorteado = random.choice(alunos) #escolhendo um nome aleatório da lista

print('O aluno escolhido foi {}'.format(sorteado))
print('-'*12)

#Faça um programa em Python que abra e reproduza um arquivo de áudio em formato mp3.
import pygame #usar o pip install pygame para instalar a biblioteca
pygame.init() #inicializa o pygame
pygame.mixer.init() #inicializa o mixer de som
pygame.mixer.music.load('ex021.mp3') #carrega o arquivo mp3, DEVE estar na mesma pasta e ter o mesmo nome
pygame.mixer.music.play() #reproduz o arquivo mp3
input('Pressione Enter para parar a reprodução') #'enter' para a reprodução parar, sem o input nao funciona
pygame.mixer.music.stop() #para a reprodução


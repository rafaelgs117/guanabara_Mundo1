#Faça um programa em Python que abra e reproduza um arquivo de áudio em formato mp3.
import pygame #usar o pip install pygame para instalar a biblioteca
pygame.init() #inicializa o pygame
pygame.mixer.init() #inicializa o mixer de som
arquivo = input("Digite o caminho do arquivo MP3: ") #caminho do arquivo mp3 abisoluto, mais nome dele .mp3
# Exemplo: C:\Users\Usuario\Desktop\musica.mp3
pygame.mixer.music.load(arquivo) #carrega o arquivo mp3
pygame.mixer.music.play() #reproduz o arquivo de som
input('Pressione Enter para parar a reprodução') #'enter' para a reprodução parar, sem o input nao funciona
pygame.mixer.music.stop() #para a reprodução


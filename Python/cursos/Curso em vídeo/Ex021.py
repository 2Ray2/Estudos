import pygame
pygame.init()
pygame.mixer.music.load('Projetos/Python/Curso em video/ex021son.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
pygame.quit()

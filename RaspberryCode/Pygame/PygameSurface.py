import pygame

pygame.init()

screen = pygame.display.set_mode((450, 450))
background = pygame.image.load("perro.jpg")
background.convert_alpha()
screen.blit(background, (0, 0))

while  True:
	pygame.display.update()
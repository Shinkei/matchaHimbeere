import pygame

pygame.init()

screen = pygame.display.set_mode((450, 450))
background = pygame.image.load("perro.jpg").convert_alpha()
theremin = pygame.image.load("gato.jpg").convert_alpha()

screen.blit(background, (0, 0))
screen.blit(theremin, (135, 50))

while True:
	pygame.display.update()
	if pygame.QUIT in [e.type for e in pygame.event.get()]:
		break

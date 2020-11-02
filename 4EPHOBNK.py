import pygame
import random

x_list = []
y_list = []

pygame.init()
win = pygame.display.set_mode((500, 500))
for y in range(6):
    x_list = []
    for x in range(6):
        x_list.append(random.randrange(0, 2))
        if x_list[x] == 0:
            pygame.draw.rect(win, (255, 255, 255), ((x-1)*20, (y-1)*20, 20, 20))
        elif x_list[x] == 1:
            pygame.draw.rect(win, (0, 0, 0), ((x-1)*20, (y-1)*20, 20, 20))
        y_list.append(x_list)
print(y_list)
print(y_list[2][3])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    pygame.display.update()

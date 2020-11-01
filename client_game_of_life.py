import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('игра в жизнь')
colored_rect_x = []
colored_rect_y = []


def background():
    for y in range(0, 500, 20):
        for x in range(0, 500, 20):
            pygame.draw.rect(win, (0, 255, 255), (x, y, 20, 20))
            pygame.draw.line(win, (0, 0, 0), (x, y), (x, y+500))
            pygame.draw.line(win, (0, 0, 0), (x, y), (x+500, y))
    x = 0
    y = 0
    for y in range(0, 500, 20):
        for x in range(0, 500, 20):
            if (x in [colored_rect_x]) and (y in [colored_rect_y]):
                pygame.draw.rect(win, (0, 0, 0), (x, y, 20, 20))


background()
pygame.display.update()
x = 0
y = 0
pygame.draw.rect(win, (255, 0, 0), (x, y, 20, 20))

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    background()
    pygame.draw.rect(win, (255, 0, 0), (x, y, 20, 20))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= 20
    if keys[pygame.K_RIGHT] and x < 480:
        x += 20
    if keys[pygame.K_UP] and y > 0:
        y -= 20
    if keys[pygame.K_DOWN] and y < 480:
        y += 20
    if keys[pygame.K_SPACE]:
        colored_rect_x.append(x)
        colored_rect_y.append(y)
    pygame.display.update()

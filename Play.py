import pygame
import random
import math
def play():
    #game window
    pygame.init()
    screen = pygame.display.set_mode((1600,900))

    #background image
    background = pygame.image.load("resized-image-Promo.png")
    screen.blit(background, [0, 0])


    #frame rate
    clock = pygame.time.Clock()

    #sphere
    def sphere():
        global cx,cy
        sphere1 = pygame.image.load("Sphere image.png")
        sphere2 = pygame.image.load("Webp.net-resizeimage.png")
        sphere_choose = [sphere1, sphere2, sphere1, sphere1]
        sphere = random.choice(sphere_choose)
        cx = random.randint(50, 1500)
        cy = random.randint(100, 800)
        screen.blit(sphere, [cx,cy])
    sphere()

    #Start
    font = pygame.font.Font("freesansbold.ttf", 28)
    start = font.render("Click the first sphere to start!", True, (255,255,255))
    screen.blit(start, (550,20))

    #Stop
    font1 = pygame.font.Font("freesansbold.ttf", 28)
    stop = font1.render("Press Alt+F4 to stop!", True, (255, 255, 255))
    screen.blit(stop, (550, 60))



    #main loop
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        click = pygame.mouse.get_pressed()

        sqx = (x - cx) ** 2
        sqy = (y - cy) ** 2

        if math.sqrt(sqx+sqy) < 80 and click[0] == 1:
            screen.blit(background, (0,0))
            sphere()

        pygame.display.update()
        clock.tick()

play()
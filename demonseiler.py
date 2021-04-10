import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
клиеокImg = pygame.image.load('зеницу.jpg')
впагImg = pygame.image.load('руи враг.jpg')
    
def  клиеок(x,y):
    gameDisplay.blit(клиеокImg, (x,y))

    
x =  (display_width * 0.45)
y = (display_height * 0.8)	#1
x2 =  (display_width * 0.10)
y2 = (display_height * 0.1)	#1
x_change = 0
y_change = 0
впаг=True


#spawn = False


while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
            #elif ebent.key == pygame.K_SPACE:
            #    spawn = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP:
                y_change = 0
        ######################
    ##
    x += x_change
    y += y_change
   ##         
    gameDisplay.fill(white)
    клиеок(x,y)
    if впаг==True:
        gameDisplay.blit(впагImg,(x2,y2))
    if (x-x2)<10 and (y-y2)<10:
        впаг=False
    

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
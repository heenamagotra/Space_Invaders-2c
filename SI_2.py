
import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

player=pygame.Rect(200,500,30,30)
playerspeed=-4
enemy=pygame.Rect(70,50,40,40)
enemyspeed= -2;
#Create a variable playerSpeed.


while True:    
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Check if left arrow key is pressed
            #move the player rectangle towards left
        
  
    enemy.x= enemy.x + enemyspeed
    
    if enemy.x == 0:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
    if enemy.x == 380:
        enemyspeed=enemyspeed * -1
        enemy.y= enemy.y + 20
    
           
    pygame.draw.rect(screen,(123,200,100),enemy)
    pygame.draw.rect(screen,(23,100,100),player)
    
    
    pygame.display.update()
    clock.tick(30)


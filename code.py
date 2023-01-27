import pygame
from random import randint

pygame.init()
width, height = 400, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('WOFFY GAME')
running = True
Green = (0,200,0)
Blue = (0,0,255)
Red = (255,0,0) 
clock = pygame.time.Clock()
Black = (0,0,0)
Yellow = (255,255,0)

pausing = False
Tube_width = 50
Tube1_x = 600
Tube2_x = 800
Tube3_x = 1000
Tube1_height = randint(100,400)
Tube2_height = randint(100,400)
Tube3_height = randint(100,400)
Tube_velocity = 3
Tube_gap = 150
Bird_x = 50
Bird_y = 400
Bird_width = 35
Bird_height = 35
Bird_drop_velocity = 0
Gravity = 0.5
Score = 0
font = pygame.font.SysFont("sans",20)
Tube1_pass = False
Tube2_pass = False
Tube3_pass = False
background = pygame.image.load(r"C:\Users\ADMIN\OneDrive\Tài liệu\Thực hành học máy\Flappy_bird\view.jpg")
background= pygame.transform.scale(background, (400,600))
Bird_image = pygame.image.load(r"C:\Users\ADMIN\OneDrive\Tài liệu\Thực hành học máy\Flappy_bird\angry-bird-yellow-icon.png")
Bird_image = pygame.transform.scale(Bird_image, (35,35))

while running:

    clock.tick(60)
    screen.fill(Green)
    screen.blit(background,(0,0))
        
    tube1 = pygame.draw.rect(screen, Blue, (Tube1_x, 0,Tube_width, Tube1_height ))
    Tube1_x -= Tube_velocity
    
    tube2 = pygame.draw.rect(screen, Blue, (Tube2_x, 0,Tube_width, Tube2_height ))
    Tube2_x -= Tube_velocity
    
    tube3 = pygame.draw.rect(screen, Blue, (Tube3_x, 0,Tube_width, Tube3_height ))
    Tube3_x -= Tube_velocity
    
    tube4 = pygame.draw.rect(screen, Blue, (Tube1_x,Tube1_height + Tube_gap, Tube_width, height - Tube1_height - Tube_gap ))
    
    tube5 = pygame.draw.rect(screen, Blue, (Tube2_x,Tube2_height + Tube_gap, Tube_width, height - Tube2_height - Tube_gap ))
    
    tube6 = pygame.draw.rect(screen, Blue, (Tube3_x,Tube3_height + Tube_gap, Tube_width, height - Tube3_height - Tube_gap ))
    
    Bird_rect = screen.blit(Bird_image,(Bird_x, Bird_y))
    
    Bird_y += Bird_drop_velocity
    Bird_drop_velocity += Gravity
    
    
    if Tube1_x < - Tube_width:
        Tube1_x = 550
        Tube1_height = randint(100,400)
        Tube1_pass = False
        
    if Tube2_x < - Tube_width:
        Tube2_x = 550
        Tube2_height = randint(100,400)
        Tube2_pass = False
        
    if Tube3_x < - Tube_width:
        Tube3_x = 550
        Tube3_height = randint(100,400)
        Tube3_pass = False
     
    if Tube1_x + Tube_width <= Bird_x and Tube1_pass == False:
        Score += 1    
        Tube1_pass = True
        
    if Tube2_x + Tube_width <= Bird_x and Tube2_pass == False:
        Score += 1
        Tube2_pass = True
    
    if Tube3_x + Tube_width <= Bird_x and Tube3_pass == False:
        Score += 1 
        Tube3_pass = True
        
    for item in [tube1,tube2,tube3,tube4,tube5,tube6]:
        if Bird_rect.colliderect(item) or Bird_y > height:
            pausing = True
            Tube_velocity = 0
            Bird_drop_velocity = 0
            Game_over = font.render("Game over, score : " + str(Score), True,Yellow )
            screen.blit(Game_over, (200,300))
            Game_continue = font.render("Press Sppace to continue ...", True,Yellow )
            screen.blit(Game_continue, (200,400))
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Bird_drop_velocity = 0
                Bird_drop_velocity -= 8
                if pausing:
                    Bird_y = 400
                    Tube1_x = 600
                    Tube2_x = 800
                    Tube3_x = 1000
                    Tube_velocity = 3
                    Score = 0
                    pausing = False  
                    
                    
                    
                    
    score_txt = font .render("Score: "  + str(Score), True, Yellow)
    screen.blit(score_txt, (5,5))
    pygame.display.flip()

pygame.quit()

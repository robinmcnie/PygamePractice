import time
import pygame
import animation
from playsound import playsound
from pygame.locals import *

pygame.init()


DISPLAYSURF = pygame.display.set_mode((1620, 1080))
pygame.display.set_caption('My_sizeGame')

character = pygame.image.load('character2.png').convert_alpha()
idle = animation.Animate(character)

SCREENWIDTH = DISPLAYSURF.get_width()
SCREENHEIGHT = DISPLAYSURF.get_height()

x_size = 50
y_size = 50
width = 40
height = 60
vel = 20
white = (255,255,255)


bg_img = pygame.image.load('1620x1080.jpg')
bg_img = pygame.transform.scale(bg_img, (1620, 1080))


animation_list = []

animation_steps = [4, 4, 4, 4, 4, 15]

action = 0

last_update = pygame.time.get_ticks()
animation_cooldown = 200
frame = 0
step_counter = 0




for animations in animation_steps:
    temp_img_list = []
    for _ in range(animations):
        temp_img_list.append(idle.get_image(step_counter, 50, 65, 3, white))
        step_counter += 1
    animation_list.append(temp_img_list)

#draws window
# def draw_window():
#     DISPLAYSURF.fill((200,150,200))
#     pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (x_size, y_size, width, height))
    
#     if action == 0:
#         DISPLAYSURF.blit(animation_list[action][frame], (x_size, y_size))
#     pygame.display.update()

# main loop
musicRun = False
run = True
while run:
    DISPLAYSURF.blit(bg_img,(0,0))
    
    if not musicRun:
        playsound('gamesongpractice.mp3', block=False)
        musicRun = True
        

    
    current_time = pygame.time.get_ticks()
    

    # if action == 5:
    #     if current_time - last_update >= animation_cooldown:
    #         frame += 1
    #         last_update = current_time
    #     if frame >= 15:
    #         frame = 0
    #         DISPLAYSURF.blit(animation_list[action][frame], (x_size, y_size))
    # else:
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
    if frame >= len(animation_list[action]):
        frame = 0
    DISPLAYSURF.blit(animation_list[action][frame], (x_size, y_size))
        
        
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x_size > vel:
        if keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and y_size< SCREENHEIGHT - height - vel:
            y_size+= vel
            x_size-= vel
            up = False
            down = True
            left = True
            right = False
            action = 5
            
        elif keys[pygame.K_UP] and y_size> vel:
            y_size-= vel
            x_size-= vel
            up = True
            down = False
            left = False
            right = True
            action = 5
            
        else:
            x_size -= vel
            left = True
            right = False
            frame = 0
            action = 2
            

    elif keys[pygame.K_RIGHT] and x_size < SCREENWIDTH - width - (vel * 4):
        if keys[pygame.K_DOWN] and y_size< SCREENHEIGHT - height - vel:
            y_size+= vel
            x_size += vel
            up = False
            down = True
            left = False
            right = True
            action = 5
            
        elif keys[pygame.K_UP] and y_size> vel:
            y_size-= vel
            x_size += vel
            up = True
            down = False
            left = False
            right = True
            action = 5
            
        else:
            x_size += vel
            left = False
            right = True
            action = 1

            
            
        
    elif keys[pygame.K_UP] and y_size> vel:
        y_size-= vel
        up = True
        down = False
        action = 3
        
        
    
    elif keys[pygame.K_DOWN] and y_size< SCREENHEIGHT - height - vel:
        
        y_size+= vel
        up = False
        down = True
        action = 4
        
        
    elif keys[pygame.K_SPACE]:
        
        action = 5
            
            
        
        
        
        
        
    else:
        left = False
        right = False
        up = False
        down = False
        walkCount = 0
        action = 0
        
        

    
    # write code to allow the character to move around the screen
    
    

    

    pygame.display.update()
    # draw_window()

pygame.quit()
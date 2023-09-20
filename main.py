import pygame
import random 

pygame.init()

#initials
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crazy Pong")
run = True
direction = [0,1]
angle = [0,1,2]

#colours in rgb format
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)

#ball (radius in pixel, ball coordinates)
radius = 15
ball_x, ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
ball_set_x, ball_set_y = 0.3, 0.3
ball_vel_x, ball_vel_y = 0.2,0.2

#Paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH-(100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

#main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type ==pygame.QUIT:
            run = False
        elif i.type ==pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel =-0.4
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.4 
            if i.key == pygame.K_w:
                left_paddle_vel =-0.4
            if i.key == pygame.K_s:
                left_paddle_vel = 0.4  
        if i.type == pygame.KEYUP:
              right_paddle_vel = 0
              left_paddle_vel = 0
    #BALL'S MOVEMENT CONTROL
    if (ball_y <= 0 + radius) or (ball_y >= HEIGHT - radius):
        ball_vel_y*= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -2*ball_set_y, ball_set_x
            if ang == 1:
                ball_vel_y,ball_vel_x = -1*ball_set_y, ball_set_x
            if ang == 2:
                ball_vel_y,ball_vel_x = -1*ball_set_y, 2*ball_set_x
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 2*ball_set_y, ball_set_x
            if ang == 1:
                ball_vel_y,ball_vel_x = 1*ball_set_y, ball_set_x
            if ang == 2:
                ball_vel_y,ball_vel_x = 1*ball_set_y, 2*ball_set_x
        ball_vel_x *= -1

    if ball_x <=0 + radius:
        ball_x, ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -2*ball_set_y, ball_set_x
            if ang == 1:
                ball_vel_y,ball_vel_x = -1*ball_set_y, ball_set_x
            if ang == 2:
                ball_vel_y,ball_vel_x = -1*ball_set_y, 2*ball_set_x
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 2*ball_set_y, ball_set_x
            if ang == 1:
                ball_vel_y,ball_vel_x = 1*ball_set_y, ball_set_x
            if ang == 2:
                ball_vel_y,ball_vel_x = 1*ball_set_y, 2*ball_set_x

        
    #paddle's movement control
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0
    
    #paddle collisions
    #left paddle collisons
    #check if x position of ball is within the range of the paddle's x position
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    #right paddle collisions
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1
                
    #movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    
    #objects      
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y),radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    pygame.display.update()
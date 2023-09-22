from ast import While
import pygame
import random 

pygame.init()

gadget_pair = 1
ch = int(input("Enter your choice for gadget pair: "))
if ch == 1:
    gadget_pair = 1
elif ch == 2:
    gadget_pair = 2
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
WHITE = (255,255,255)

#ball (radius in pixel, ball coordinates)
radius = 15
ball_x, ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
ball_set_x, ball_set_y = 0.2, 0.2
ball_vel_x, ball_vel_y = 0.2,0.2
#creation of phantom ball
phantom_ball_x, phantom_ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
phantom_ball_set_x, phantom_ball_set_y = 0.2, 0.2
phantom_ball_vel_x, phantom_ball_vel_y = 0.2,0.2
#Paddle dimensions
paddle_width= 20
left_paddle_height = right_paddle_height = 120
left_paddle_y = HEIGHT/2 - left_paddle_height/2
right_paddle_y = HEIGHT/2 - right_paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH-(100 - paddle_width/2)
right_paddle_vel = left_paddle_vel = 0

#gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 4

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
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1
            if i.key == pygame.K_LEFT and right_gadget_remaining > 0:
                right_gadget =2
            if i.key == pygame.K_w:
                left_paddle_vel =-0.4
            if i.key == pygame.K_s:
                left_paddle_vel = 0.4
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1
            if i.key == pygame.K_a and left_gadget_remaining > 0:
                left_gadget = 2
                
        if i.type == pygame.KEYUP:
              right_paddle_vel = 0
              left_paddle_vel = 0
    #BALL'S MOVEMENT CONTROL
    if (ball_y <= 0 + radius) or (ball_y >= HEIGHT - radius):
        ball_vel_y*= -1
    if (phantom_ball_y <= 0 + radius) or (phantom_ball_y >= HEIGHT - radius):
        phantom_ball_vel_y*= -1
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
        phantom_ball_x, phantom_ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
        #to reset the paddles
        left_paddle_height = right_paddle_height = 120
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.75*ball_set_y, ball_set_x
                phantom_ball_vel_y, phantom_ball_vel_x = -1.75*phantom_ball_set_y, phantom_ball_set_x
            if ang == 1:
                ball_vel_y,ball_vel_x = -1*ball_set_y, ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = -1*phantom_ball_set_y, phantom_ball_set_x
            if ang == 2:
                ball_vel_y,ball_vel_x = -1*ball_set_y, 2*ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = -1*phantom_ball_set_y, 2*phantom_ball_set_x
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.75*ball_set_y, ball_set_x
                phantom_ball_vel_y, phantom_ball_vel_x = 1.75*phantom_ball_set_y, phantom_ball_set_x
            if ang == 1:
                ball_vel_y,ball_vel_x = 1*ball_set_y, ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = 1*phantom_ball_set_y, phantom_ball_set_x
            if ang == 2:
                ball_vel_y,ball_vel_x = 1*ball_set_y, 1.75*ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = 1*phantom_ball_set_y, 1.75*phantom_ball_set_x

        ball_vel_x *= -1
        phantom_ball_vel_x *= -1
        
    if ball_x <=0 + radius:
        ball_x, ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
        phantom_ball_x, phantom_ball_y = WIDTH/2 - radius,  HEIGHT/2 - radius
        #to reset the paddles
        left_paddle_height = right_paddle_height = 120        
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.5*ball_set_y, ball_set_x
                phantom_ball_vel_y, phantom_ball_vel_x = -1.5*phantom_ball_set_y, phantom_ball_set_x
            if ang == 1:
                ball_vel_y,ball_vel_x = -1*ball_set_y, ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = -1*phantom_ball_set_y, phantom_ball_set_x
            if ang == 2:
                ball_vel_y,ball_vel_x = -1*ball_set_y, 1.5*ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = -1*phantom_ball_set_y, 1.5*phantom_ball_set_x
        if dir == 1:
            if ang == 0:
                ball_vel_y,ball_vel_x = 1.5*ball_set_y, ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = 1.5*phantom_ball_set_y, phantom_ball_set_x
            if ang == 1:
                ball_vel_y,ball_vel_x = 1*ball_set_y, ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = 1*phantom_ball_set_y, phantom_ball_set_x
            if ang == 2:
                ball_vel_y,ball_vel_x = 1*ball_set_y, 1.5*ball_set_x
                phantom_ball_vel_y,phantom_ball_vel_x = 1*phantom_ball_set_y, 1.5*phantom_ball_set_x


        
    #paddle's movement control
    if left_paddle_y >= HEIGHT - left_paddle_height:
        left_paddle_y = HEIGHT - left_paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - right_paddle_height:
        right_paddle_y = HEIGHT - right_paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0
    
    #paddle collisions
    #left paddle collisons
    #check if x position of ball is within the range of the paddle's x position
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + left_paddle_height:
            ball_x = left_paddle_x + paddle_width
            phantom_ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
            phantom_ball_vel_x *= -1
    #right paddle collisions
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + right_paddle_height:
            ball_x = right_paddle_x
            phantom_ball_x = right_paddle_x
            ball_vel_x *= -1
            phantom_ball_vel_x *= -1

    #gadgets in action
    # gadget 1 is slam
    if gadget_pair == 1:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + left_paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -3
                    phantom_ball_vel_x *= -3
                    left_gadget = 0
                    left_gadget_remaining -= 1
        #gadget 2 is flash
        elif left_gadget == 2:
            left_paddle_y = ball_y
            left_gadget = 0
            left_gadget_remaining -= 1 
                
        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + right_paddle_height:
                    ball_x = right_paddle_x
                    ball_vel_x *= -3
                    phantom_ball_vel_x *= -3
                    right_gadget = 0
                    right_gadget_remaining -= 1
        elif right_gadget == 2:
            right_paddle_y = ball_y
            right_gadget = 0
            right_gadget_remaining -= 1
    #second pair gadget
    elif gadget_pair == 2:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + left_paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    phantom_ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -1
                    phantom_ball_vel_x *= -1
                    phantom_ball_vel_y *= -1
                    left_gadget = 0
                    left_gadget_remaining -= 1
        elif left_gadget == 2:
            left_paddle_height = left_paddle_height * 1.75
            left_gadget = 0
            left_gadget_remaining -= 1 
            
        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + right_paddle_height:
                    ball_x = right_paddle_x
                    phantom_ball_x = right_paddle_x
                    ball_vel_x *= -1
                    phantom_ball_vel_x *= -1
                    phantom_ball_vel_y *= -1
                    right_gadget = 0
                    right_gadget_remaining -= 1
        elif right_gadget == 2:
            right_paddle_height = right_paddle_height * 1.75
            right_gadget = 0
            right_gadget_remaining -= 1                 
        
    #movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    phantom_ball_x += phantom_ball_vel_x
    phantom_ball_y += phantom_ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    
    #objects      
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y),radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, left_paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, right_paddle_height))
    
    #phantom ball
    pygame.draw.circle(wn, BLUE, (phantom_ball_x, phantom_ball_y),radius)

    #small circle with radius of 4 to indicate activated slam function
    if left_gadget == 1:
        pygame.draw.circle(wn, WHITE,(left_paddle_x + 10,left_paddle_y +10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn, WHITE,(right_paddle_x + 10,right_paddle_y +10), 4)
        
    pygame.display.update()
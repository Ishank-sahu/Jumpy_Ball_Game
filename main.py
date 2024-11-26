import pygame
import random
import os

# Display
pygame.init()
gamewindow= pygame.display.set_mode((700,700)) 
pygame.display.set_caption('Jumpy Ball')

# Colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#Coordinates
bx = 350
by = 200
p1y = 175
p2y = 350
p3y = 525
p4y = 699
p1x = 200
p2x = 300
p3x = 330
p4x = 150
hr_x =400 

#Variables
vel_x = 10
vel_y = 20
radius = 17
jump = False
run = False
falling = True
i =0
width = 700
death = False 
sc = 0
y = 500
x=0
width = 700
start = True
cont = False
scale = 0.3
jsound = 0
hr = 0
pvel=3

#Music
ham = pygame.mixer.Sound('media/hum.wav')
pygame.mixer.Sound.set_volume(ham,0.05)
wee = pygame.mixer.Sound('media/wee.wav')
pygame.mixer.Sound.set_volume(wee,0.05)
pygame.mixer.music.load('media/heli.wav')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.05)
wee2 = pygame.mixer.Sound('media/wee2.mp3')
wee3 = pygame.mixer.Sound('media/wee3.mp3')
wee4 = pygame.mixer.Sound('media/wee4.mp3')
wee5 = pygame.mixer.Sound('media/wee5.mp3')
pygame.mixer.Sound.set_volume(wee2,0.05)
pygame.mixer.Sound.set_volume(wee3,0.05)
pygame.mixer.Sound.set_volume(wee4,0.05)
pygame.mixer.Sound.set_volume(wee5,0.05)

#Images
bg_img = pygame.image.load('media/bg.jpg')
bg = pygame.transform.scale(bg_img,(700,700))
go_img = pygame.image.load('media/go.png')
go = pygame.transform.scale (go_img,(500,300))
bg_img = pygame.image.load('media/bg.jpg')
bg = pygame.transform.scale(bg_img,(700,700))
logo_img = pygame.image.load('media/logo.png')
logo = pygame.transform.scale(logo_img,(500,230))
sahu_g_img = pygame.image.load('media/Sahu G.png')
Sahu_G = pygame.transform.scale(sahu_g_img,(100,200)) 
start_img = pygame.image.load('media/start.png')
control_img = pygame.image.load('media/control.png')
start_width= start_img.get_width()
Start_height = start_img.get_height()
control_width = control_img.get_width()
control_height = control_img.get_height()
start_logo = pygame.transform.scale(start_img,[int(start_width*scale),int(Start_height*scale)])
control_logo = pygame.transform.scale(control_img,[int(control_width*scale),int(control_height*scale)])
button_img = pygame.image.load('media/button.png')
button = pygame.transform.scale(button_img,[int(button_img.get_width()*0.8),int(button_img.get_height()*0.8)])
back_img = pygame.image.load('media/back.png')
back = pygame.transform.scale(back_img,[int(back_img.get_width()*0.7),int(back_img.get_height()*0.7)])

#rect of logo
start_rect = pygame.Rect(230,380,int(start_width*scale),int(Start_height*scale))
control_rect = pygame.Rect(230,500,int(control_width*scale),int(control_height*scale))
back_rect = pygame.Rect(-10,7,int(back_img.get_width()*0.7),int(back_img.get_height()*0.7))

#Text
font = pygame.font.SysFont('Baskerville Old Face',40)
font1 = pygame.font.SysFont('Gabriola',75)
font2 = pygame.font.SysFont('Baskerville Old Face',30)
text2 = font2.render("Sahu G Studio present",True,black)
text3 = font1.render("Press 'R' to retry",True,black)

#main menu loop
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

   #display stuff
    gamewindow.blit(bg, (0,x))
    gamewindow.blit(bg, (0,-width+x))
    if x == width :
        x = 0
    x += 1
    y -= 2
    gamewindow.blit(logo,[70,100])
    gamewindow.blit(text2,[5,2])
    gamewindow.blit(Sahu_G,[590,y])
    gamewindow.blit(start_logo,[230,380])
    gamewindow.blit(control_logo,[230,500])
    userinput= pygame.key.get_pressed()
    
    # Mouse botton
    mouse= pygame.mouse.get_pos()

    if start_rect.collidepoint(mouse) and cont == False:
        if pygame.mouse.get_pressed()[0] == 1 :
            start = False
            pygame.mixer.music.pause()
            run = True
    
    if control_rect.collidepoint(mouse) and cont == False:
        if pygame.mouse.get_pressed()[0] == 1:
            cont = True

    #Control Pannel
    if cont == True:
        gamewindow.blit(bg, (0,x))
        gamewindow.blit(bg, (0,-width+x))
        if x == width :
            x = 0
        x += 1
        gamewindow.blit(button,(180,150))
        gamewindow.blit(back,(-10,7))

        if back_rect.collidepoint(mouse): 
            if pygame.mouse.get_pressed()[0] == 1 :
                cont = False

    if userinput[pygame.K_SPACE] and cont == False:
        start = False
        pygame.mixer.music.pause()
        run = True

    pygame.time.delay(25)
    pygame.display.update()

if run:
    ham.play()

# Game Loop
while run:
    userinput= pygame.key.get_pressed()
    
    
    #BG 
    gamewindow.blit(bg, (0,i))
    gamewindow.blit(bg, (0,-width+i))
    if i == width :
        i = 0
    i += 1

    # Main Character
    pygame.draw.circle(gamewindow,red,(bx,by),radius)
    pygame.draw.circle(gamewindow,black,(bx,by),radius,3)
    ball = pygame.Rect(bx-15,by+14,30,15)
    #pygame.draw.rect(gamewindow,white,ball,2)
    
    # Quit when press cross
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    if userinput [pygame.K_a]:
         bx -= vel_x
    if userinput [pygame.K_d]:
        bx += vel_x
    if  userinput[pygame.K_SPACE] and not falling:
            jump = True
            jsound += 1 

            #Jump Sound
            if jsound == 1:
                wee.play()
            if jsound == 2:
                wee2.play()
            if jsound == 3:
                wee3.play()
            if jsound == 4:
                wee4.play()
            if jsound == 5:
                wee5.play()
                jsound = 0
    if jump :
       by-=vel_y*1.8
       vel_y -=1
    if vel_y==0:
        vel_y=20
        jump = False
    if falling:
        by +=vel_x
    if falling==False:
        by += pvel
    if bx == 0:
        bx = 690
    if bx == 700:
        bx = 0

    #Score
    if os.path.exists('highscore.txt'):
        hs=open('highscore.txt','r')
        hr=int(hs.read())
        hs.close()
    if not death:
        sc += 1
    text4 = font.render('High Score: '+str(hr),True,black)
    text = font.render('Score: '+str(sc),True,black)
    gamewindow.blit(text,[5,5])
    gamewindow.blit(text4,[hr_x,5])
    if sc>1000:
        pvel=5
    if 1000>sc>500:
        pvel=4
    if sc<500:
        pvel=3
    
    
    # Platforms
    if p1y > 700:
        p1x = random.randint(20,595)
        p1y = 0
    p1y += pvel
    
    pygame.draw.rect(gamewindow,black,[p1x,p1y,70,5])
    p1 = pygame.Rect(p1x,p1y,70,5) 

    if p2y > 700:
       p2x = random.randint(10,595)
       p2y = 0
    p2y += pvel
    pygame.draw.rect(gamewindow,black,[p2x,p2y,70,5])
    p2 = pygame.Rect(p2x,p2y,70,5)

    if p3y > 700:
       p3x = random.randint(10,595)
       p3y = 0
    p3y += pvel
    pygame.draw.rect(gamewindow,black,[p3x,p3y,70,5])
    p3= pygame.Rect(p3x,p3y,70,5)
     
    if p4y > 700:
       p4x = random.randint(10,595)
       p4y = 0
    p4y += pvel
    pygame.draw.rect(gamewindow,black,[p4x,p4y,70,5])
    p4 = pygame.Rect(p4x,p4y,70,5)

    # Collision 
    if ball.colliderect(p1) or ball.colliderect(p2) or ball.colliderect(p3) or ball.colliderect(p4) :
        falling=False
    if jump or not ball.colliderect(p1) and not ball.colliderect(p2) and not ball.colliderect(p3) and not ball.colliderect(p4):
        falling=True  

    # Death
    if by > 700:
        death = True
     
    
    if death:
        gamewindow.blit(go,(100,100))
        gamewindow.blit(text3,[165,500])
        if hr < sc:
            hr=sc
            hs=open('highscore.txt','w')
            hs.write(str(sc))
            hs.close()
            
        
    if death and userinput[pygame.K_r]:
        death = False
        bx = 350
        by = 100
        ham.play()
        sc = 0
        jsound=0

    pygame.time.delay(25)
    pygame.display.update()


pygame.quit()

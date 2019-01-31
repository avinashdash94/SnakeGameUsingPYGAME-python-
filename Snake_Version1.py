#****Note: in this we take all code in a function gameloop() and call that  at end
import pygame
import random # import random module for  to be displayed randomly in any position of window
import os # used to if the hiscore file is deleted it will show an error so if there is no file the it should create automaticaly
pygame.mixer.init()# to initilised the mixer for music(to add music in game)
# pygame.mixer.music.load('sound/intro.ogg')# here we load the music
# pygame.mixer.music.play()# to play the song
# BackGrounnd image
# bgimg=pygame.image.load('')
# bgimg=py.transform.scale(bgimg,(screen_width,screen_height))
pygame.init()# initilises all the modules of pygame

#Colors 
white=(255,255,255) # we use RGB color having valule 0 t0 256
red=(255,0,0)
black=(0,0,0)
   
screen_width=900
screen_height=600

#Creating window
gameWindow=pygame.display.set_mode((screen_width,screen_height))# it will create window for game thah take a single argument we pass tuple
#creating image
image_during_play=pygame.image.load('screen/play.jpg')
image_during_play=pygame.transform.scale(image_during_play,(screen_width,screen_height)).convert_alpha()#transform the image to window size 'convert alpha' use  when we blit the img it dont effet the game speed
#game Title
pygame.display.set_caption("Snake With Avinash")
pygame.display.update()#is used to update if any change we have done on display( to see the changes on display)
#Creating "clock for action" accodring to time
clock=pygame.time.Clock()
#creating  "font variable" for score
font =pygame.font.SysFont(None, 55)# None means default system font  and 55 means size of font


#"sco"r on windows
def text_screen(text,color,x,y): # parameters are what text i want to print  what color and (x,y)position
    screen_text=font.render(text,True, (15,6,200))# render is function of pygame.font 'True' for antialysing
    gameWindow.blit(screen_text,[x,y]) # to update the screen_text
# function to "create snake " 
def plot_snake(gameWindow,color,snk_list,snake_size):
    # print(snk_list) # we can print this list and see the how it grows
    for x,y in snk_list: # due to this snk-list new rectangels were add with in list
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

#function to create "welcome page"  before sart the game like in other game 
def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill((200,10,10))# First fill the whole color of the scree by white
        gameWindow.blit(image_welcome,(0,0))
        # text_screen("Welcome to Snakes",black,260,250)
        # text_screen("Press Space Bar To Play",black,235,290)
        ####### i can do as above three line or can add an image##### 
        #****** Image for Welcome PAge*****
        # BackGrounnd image
        

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:# if Enter key used to start 
                # if event.key==pygame.K_SPACE:# for space key to start game
                    image_over=pygame.image.load('screen/snakeWelcome.png')
                    image_over=pygame.transform.scale(image_over,(screen_width,screen_height)).convert_alpha()#transform the image to window size 'convert alpha' use  when we blit the img it dont effet the game speed


                    pygame.mixer.music.load('sound/playGame.ogg')# here we load the music
                    pygame.mixer.music.play()# to play the song
                    gameloop()
        
        pygame.display.update()
        clock.tick(60)

# defining  method for game over
def gameloop():
    #Game specific  variable
    exit_game=False
    game_over=False
    snake_x=45 #for initial positiion in x
    snake_y=55 # for initial position in y
    snake_size=15 # size of snake  for both x and y as make an rectagle
    init_velocity=5# for initial velocit so that if we change velocity in future not to change variable every time
    velocity_x=0 #velocity in x direction initialy 0 as in starting it is stop
    velocity_y=0 # veocity in y directioninitialy 0 as in starting it is stop
    food_x=random.randint(20,screen_width/2)# for randomly food come in any position random module contane randInt() method where we give range to choose no 0 to width(900) of window
    food_y=random.randint(20,screen_height/2)#  random module contane randInt() method where we give range to choose no 0 to heigth(600) of window

    #to Check if hisocer file exites or not if not then it will create it automaticaly
    if not os.path.exists("hiscore.txt"):# if file not exit in directory
        with open("hiscore.txt","w") as f:# if we opoen file in write mode it will automaticaly generate file if not exist
            f.write("0")

    #to store hight score in file i.e is hiscore.text 
    with open("hiscore.txt","r") as f:
        hiscore=f.read()

    score=0 # to display score on display
    fps=60 # frame per second change frame at this interval(fps=how many frame you want in a second)
    snk_list=[] # for increasing lenght of snake append hear
    snk_length=1 # initial length =1 as only one squar block is there


    #Game Loop so that window will not close automaticaly
    while not exit_game:
        if game_over: # when game over become true
            #save high score on hiscore.txt file 
            with open("hiscore.txt","w") as f: # open file in write mode
                f.write(str(hiscore))
            gameWindow.fill(white)# when the game over screen become white 
            text_screen("Game Over ! Press Enter To continue",red,100,250)# call text_scree to print text at position half of width and height
            image_over=pygame.image.load('screen/over.png')
            image_over=pygame.transform.scale(image_over,(screen_width,screen_height)).convert_alpha()#transform the image to window size 'convert alpha' use  when we blit the img it dont effet the game speed
            gameWindow.blit(image_over,(0,0))
            text_screen("Your Score:"+str(score),red,300,350)

            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        # gameloop()
                        pygame.mixer.music.load('sound/intro.ogg')# here we load the music
                        pygame.mixer.music.play()# to play the song
                        welcome()# now call welcome when it gameover after pressing enter
        else:
            for event in pygame.event.get():
                # print(event)
                if event.type==pygame.QUIT:
                    exit_game=True          

                if event.type==pygame.KEYDOWN:# event When any key is pressed
                    if event.key==pygame.K_RIGHT:# if Right key is preased
                        # snake_x=snake_x+10
                        velocity_x=init_velocity#when we click in Right buttn then it shoud move in x direction only not in y
                        velocity_y=0# to stop movement in y direction
                    if event.key==pygame.K_LEFT:
                        # snake_x=snake_x-10
                        velocity_x=-init_velocity#when we click in left buttn then it shoud move in x direction only not in y
                        velocity_y=0# to stop movement in y direction

                    if event.key==pygame.K_UP:
                        # snake_y=snake_y-10
                        velocity_y=-init_velocity#when we click in up buttn then it shoud move in y direction only not in x
                        velocity_x=0# to stop movement in x direction
                    if event.key==pygame.K_DOWN:
                        # snake_y=snake_y+10
                        velocity_y=init_velocity#when we click in down buttn then it shoud move in y direction only not in x
                        velocity_x=0# to stop movement in x direction

                    #cheat codes
                    if event.key==pygame.K_q:#if you want to inscrease score without eating food press 'q' key to increase automaticaly
                        score+=5
            
            snake_x= snake_x+ velocity_x
            snake_y= snake_y+ velocity_y
            # we take absulute value as it is posible when snake come near and only just touch the food at that time if diffrerence not 0 food position will not change so for tha t we take absulute vale
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:  
                score+=10
                # print("Score ",score*10)
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_height/2)
                snk_length+=5 #we take 5 as we adding cordinate
                # storing high score in hiscore.txt file
                if score>int(hiscore):
                    hiscore=score

            gameWindow.fill(white)
            gameWindow.blit(image_during_play,(0,0))
            # to print score
            text_screen("Score: "+str(score)+ "  Hiscore: "+str(hiscore), red ,5,5)# "Score :"+str(score*10) is a single argument of method which is string so we convert scor to str
            
            #Creating food for snake
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])# red color is defined above in rgb form

            head=[] #as there is initialy a head in snake
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head) # add thathead to snk_list

            if len(snk_list)>snk_length:# when value in snake list is greateer the the lenth of snake it delete the extre appended snake 
                del snk_list[0] # we do so as if we dont do that snake will increase automaticaly as in while loop
            
            # if snake touch it self then game over
            if head in snk_list[:-1]:# if the cordinate  of head is in the list means snake touch itself except head i.e(-1)
                game_over=True
                pygame.mixer.music.load('sound/over.ogg')# here we load the music
                pygame.mixer.music.play()# to play the song
            # if snake go out of the boundries 
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height: 
                
                game_over=True
                # gameWindow.blit(image_over,(0,0))
                pygame.mixer.music.load('sound/over.ogg')# here we load the music
                pygame.mixer.music.play()# to play the song
                # print("Game Over")

            #head of snake 
            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size]) #we created head by  creating rectangle
            plot_snake(gameWindow,black,snk_list,snake_size) # Createing a saperate function to create snake as it is increasing

        pygame.display.update()#is used to update if any change we have done on display
        clock.tick(fps)# changing frame ie inside the while loop(fps=how many frame you want in a second)




    pygame.quit()
    quit()

image_welcome=pygame.image.load('screen/snakeWelcome.png')
image_welcome=pygame.transform.scale(image_welcome,(screen_width,screen_height)).convert_alpha()#transform the image to window size 'convert alpha' use  when we blit the img it dont effet the game speed
pygame.mixer.music.load('sound/intro.ogg')# here we load the music
pygame.mixer.music.play()# to play the song
welcome()
# gameloop()


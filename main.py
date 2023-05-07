import pygame

pygame.init()


#width and height of game window, can change these values 
#to adjust to user's screen
width = 800
height =800
game_window = pygame.display.set_mode(  (width,height) )

white_color = (255,255,255)

clock = pygame.time.Clock() 

#load background image
background_image = pygame.image.load('asset/background.png')
#scale background image
background = pygame.transform.scale(background_image,(width,height))

def run_game_loop():
    while True:
        #handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

        #Execute logic
        #Update display
        game_window.fill(white_color)
        game_window.blit(background,(0,0))
        pygame.display.update()

        clock.tick(60)

run_game_loop()        

pygame.quit()
quit()

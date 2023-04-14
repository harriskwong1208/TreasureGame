import pygame

pygame.init()


#width and height of game window, can change these values 
#to adjust to user's screen
width = 800
height =800
game_window = pygame.display.set_mode(  (width,height) )

white_color = (255,255,255)

clock = pygame.time.Clock() 

while True:
    #handle events
    #Execute logic
    #Update display
    game_window.fill(white_color)
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()

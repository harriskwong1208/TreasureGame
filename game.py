import pygame
from gameObject import GameObject


class Game:

    def __init__(self):
        #width and height of game window, can change these values 
        #to adjust to user's screen
        self.width = 800
        self.height =800
        self.game_window = pygame.display.set_mode(  (self.width,self.height) )

        self.white_color = (255,255,255)

        self.clock = pygame.time.Clock() 


        self.background = GameObject(0,0,self.width,self.height,'asset/background.png')
        self.treasure = GameObject(375,50,50,50,'asset/treasure.png')
     


    def draw_objects(self):
        self.game_window.fill(self.white_color)
            
        #set image where on the screen 
        self.game_window.blit(self.background.image,(self.background.x,self.background.y))
        self.game_window.blit(self.treasure.image,(self.treasure.x,self.treasure.y))
        pygame.display.update()




    def run_game_loop(self):
        while True:
            #handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return

            #Execute logic
            #Update display
            self.draw_objects()

            self.clock.tick(60)        
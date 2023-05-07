import pygame


class Game:

    def __init__(self):
        #width and height of game window, can change these values 
        #to adjust to user's screen
        self.width = 800
        self.height =800
        self.game_window = pygame.display.set_mode(  (self.width,self.height) )

        self.white_color = (255,255,255)

        self.clock = pygame.time.Clock() 

        #load images
        background_image = pygame.image.load('asset/background.png')
        treasure_image = pygame.image.load('asset/treasure.png')



        #scale background image
        self.background = pygame.transform.scale(background_image,(self.width,self.height))
        self.treasure = pygame.transform.scale(treasure_image,(50,50))


    def draw_objects(self):
        self.game_window.fill(self.white_color)
            
        #set image where on the screen 
        self.game_window.blit(self.background,(0,0))
        self.game_window.blit(self.treasure,(375,50))
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
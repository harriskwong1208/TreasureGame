import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

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
        self.player = Player(375,700,50,50,'asset/player.png',7)

        self.enemies = [
            Enemy(0,600,50,50,'asset/enemy.png',7),
            Enemy(750,400,50,50,'asset/enemy.png',7),
            Enemy(0,200,50,50,'asset/enemy.png',7)
        ]

        


    def draw_objects(self):
        self.game_window.fill(self.white_color)
            
        #set image where on the screen 
        self.game_window.blit(self.background.image,(self.background.x,self.background.y))
        self.game_window.blit(self.treasure.image,(self.treasure.x,self.treasure.y))
        self.game_window.blit(self.player.image,(self.player.x,self.player.y))
       
        for enemy in self.enemies:
            self.game_window.blit(enemy.image,(enemy.x,enemy.y))

        pygame.display.update()


    def move_object(self,player_direction):
        self.player.move(player_direction,self.height)
        for enemy in self.enemies:
            enemy.move(self.width)


    def detect_collision(self,object_1,object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        
        return True
        
    def check_if_collided(self):
            for enemy in self.enemies:
                if self.detect_collision(self.player,enemy):
                    return True
            if self.detect_collision(self.player,self.treasure):
                return True
            return False


    def run_game_loop(self):

        player_direction = 0

        while True:
            #handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    #move player up
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    #move player down    
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

                        
            #Execute logic
            self.move_object(player_direction)

            #Update display
            self.draw_objects()

            #detect collisions         
            if self.check_if_collided():
                return

            self.clock.tick(60)        
import random 
import pygame 

class Button(): 
    def __int__(self, x, y, width, pos, hight): 
        self.x = x
        self.y = y 
        self.pos = pos 
        self.width = width 
        self.hight = hight 

    def clicked(self, pos): 
        self.pos = pygame.mouse.get_pos() 

        if self.pos[0] > self.x and self.pos[0] < self.x + self.width: 
            if self.pos[1] > self.y and self.pos[1] < self.y + self.hight: 
                return True 
        return False 

class RpsGame():  

    def __init__(self): 
        pygame.init() 

        self.screen = pygame.display.set_mode(960, 640)
        pygame.display.set_caption("RPS Smasher ") 
        
        self.bg = pygame.image.load("background.jpg") 
        self.r_btn = pygame.image.load("r_button.png").convert-alpha() 
        self.p_btn = pygame.image.load("p_button.png").convert-alpha() 
        self.s_btn = pygame.image.load("s_button.png").convert-alpha()  
        
         self.choose_rock = pygame.image.load("rock.png").convert-alpha()  
         self.choose_scissors = pygame.image.load("scissors.png").convert-alpha()  
         self.choose_paper = pygame.image.load("paper.png").convert-alpha()  
        
            
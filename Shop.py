import pygame
import os
from os import path
ASSETS_FOLDER=os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER=os.path.join(ASSETS_FOLDER,'image_assets')

class shop_item():
    def __init__(self,x,y,level,description,scale,cost):
        img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'shop_button.png'))
        width=img.get_width()
        height=img.get_height()
        img=pygame.transform.scale(img,(width,height))
        self.img=pygame.transform.scale(img,(int(width)*2,int(height)*2))
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
        self.img=img
        self.level=level
        self.desc=description
        self.cost=cost
        

    def shop_spawn(self,screen):
        buy=False
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                buy=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        screen.blit(self.img,(self.rect.x,self.rect.y))
        #level display
        font=pygame.font.SysFont('calibri.ttf',18)
        level_display=font.render(str(self.level),True,(0,0,0))
        screen.blit(level_display,(self.rect.x+125,self.rect.y+9))
        
        #description Display
        font2=pygame.font.SysFont('calibri.ttf',12)
        desc_display=font2.render(str(self.desc),True,(0,0,0))
        screen.blit(desc_display,(self.rect.x+4,self.rect.y+19))
        cost_display=font2.render('Cost: $'+str(self.cost),True,(0,0,0))
        screen.blit(cost_display,(self.rect.x+4,self.rect.y+19+13))
        return buy

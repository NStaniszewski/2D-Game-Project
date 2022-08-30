import pygame
import os
from os import path
ASSETS_FOLDER=os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER=os.path.join(ASSETS_FOLDER,'image_assets')

class shop_item():
    def __init__(self,x,y,level,description,scale):
        img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'shop_button.png'))
        img=pygame.transform.scale(img,(x,y))
        width=img.get_width()
        height=img.get_height()
        self.img=pygame.transform.scale(img,(int(width*scale),int(height*scale)))
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
        self.img=img
        self.level=level
        self.desc=description
        

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
        return buy


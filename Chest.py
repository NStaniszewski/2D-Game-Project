import pygame
import math
from os import path
import os

ASSETS_FOLDER=os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER=os.path.join(ASSETS_FOLDER,'image_assets')




class Chest():
    def __init__(self,x,y,img_name,scale,bonus,multiplier):
        chest_img=pygame.image.load(os.path.join(IMAGE_FOLDER, img_name))
        chest_img=pygame.transform.scale(chest_img,((chest_img.get_width()*scale,(chest_img.get_height()*scale))))
        width=chest_img.get_width()
        self.width=width
        height=chest_img.get_height()
        self.height=height
        self.chest_img=pygame.transform.scale(chest_img,(int(width*scale),int(height*scale)))
        self.rect=self.chest_img.get_rect()
        self.rect.topleft=(x,y)
        self.bonus=bonus
        self.muli=multiplier
    
    def create(self,screen,playerX,playerY,falling):
        if playerX>=self.rect.topleft[0]-26 and playerX<=self.rect.topleft[0]+self.width-4 and playerY>=self.rect.topleft[1]:
            if falling==0 and playerX<=(self.rect.topleft[0]*2+self.width)/2:
                action=1
            elif falling==0 and playerX>=(self.rect.topleft[0]*2+self.width)/2:
                action=2
            else:
                action=3
        else:
            action=0
        screen.blit(self.chest_img,(self.rect.x,self.rect.y))
        return action
#action=0, means no collision, 1 means collision on right side, 2 means collision on left side, 3 means collision on top (will bounce)
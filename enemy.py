import os
from os import path
import pygame
import random

ASSETS_FOLDER=os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER=os.path.join(ASSETS_FOLDER,'image_assets')

class goblin():
    def __init__(self,x,y,scale,playerX,playerY,player_width,player_height,attacking,defending,action_lock):
        goblin_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'goblin.png'))
        self.img=pygame.transform.scale(goblin_img,((goblin_img.get_width()*scale,(goblin_img.get_height()*scale))))
        goblin_atk_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'goblin_atk.png'))
        self.atk_img=pygame.transform.scale(goblin_atk_img,((goblin_atk_img.get_width()*scale,(goblin_atk_img.get_height()*scale))))
        width=goblin_img.get_width()
        height=goblin_img.get_height()
        self.atk_width=goblin_atk_img.get_width()
        self.atk_height=goblin_atk_img.get_height()
        self.img=pygame.transform.scale(goblin_img,(int(width*scale),int(height*scale)))
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)
        self.width=width
        self.playerX=playerX
        self.playerY=playerY
        self.player_width=player_width
        self.player_height=player_height
        self.player_attacking=attacking
        self.player_defending=defending
        self.x=x
        self.y=y
        self.action_lock=action_lock

    def spawn(self,screen):
        atk_action=-1
        damaged=False
        if self.playerX-37>self.rect.topleft[0]:
            action=1
        elif self.playerX+self.player_width<self.rect.topleft[0]:
            action=2
        else:
            action=0
        if self.player_attacking==1 and self.playerY<=self.rect.topleft[1] and self.rect.topleft[0]<=self.playerX and self.rect.topleft[0]+self.width>=self.playerX-26:
            damaged=True
        elif self.player_attacking==1 and self.playerY<=self.rect.topleft[1] and self.rect.topleft[0]<=self.playerX+self.player_width-26 and self.rect.topleft[0]>=self.playerX-26:
            damaged=True

        if self.action_lock==0:
            if self.playerX<=self.rect.topleft[0]+self.width+4 and self.playerX>=self.rect.topleft[0]-26 and self.playerY>=self.rect.topleft[1]:
                #collision with goblin body, will take damage from collision
                atk_action=1
            elif self.playerX<=self.rect.topleft[0]+self.width+25 and self.playerX>=self.rect.topleft[0]-51 and self.playerY>=self.rect.topleft[1]:
                #goblin attacks player
                if self.player_defending==1:
                    probability=random.randrange(11)
                    #print(probability)
                    if probability<=7:
                        atk_action=3
                        if self.playerX>self.x:
                            action=2
                        elif self.playerX<self.x:
                            action=1
                    else:
                        if self.x<self.playerX:
                            atk_action=2
                        else:
                            atk_action=3
                elif self.player_defending==0:
                    if self.x<self.playerX:
                        atk_action=2
                    elif self.x>self.playerX:
                        atk_action=3
            else:
                atk_action=0
        else:
            if self.playerX>self.x:
                action=2
            elif self.playerX<self.x:
                action=1
        if atk_action==2:
            screen.blit(self.atk_img,(self.x+32,self.y+8))
            if self.playerY<=self.y+8 and self.playerY+32>=self.y+18 and self.playerX>=self.x+32 and self.playerX+32>=self.x+52:
                atk_action=-2
            #-2 means hit
        elif atk_action==3:
            screen.blit(self.atk_img,(self.x-20,self.y+8))
            #print('a')
            if self.playerY<=self.y+8 and self.playerY+32>=self.y+18 and self.playerX+32>=self.x-20 and self.playerX<=self.x:
                atk_action=-2
        screen.blit(self.img,(self.x,self.y))
        #print(action,atk_action, self.player_defending,self.x,self.playerX,self.action_lock,self.playerY,damaged)
        #print(self.playerX,self.rect.topleft[0],damaged)
        return (action,atk_action,damaged)
    
class skeleton():
    pass

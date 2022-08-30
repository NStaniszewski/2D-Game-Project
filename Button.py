import pygame

class Button():
    def __init__(self,x,y,img,scale):
        width=img.get_width()
        height=img.get_height()
        self.img=pygame.transform.scale(img,(int(width*scale),int(height*scale)))
        self.rect=self.img.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
    
    def create(self, screen):
        action=False
        mouse_pos=pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                action=True
        if pygame.mouse.get_pressed()[0]==0:
            self.clicked=False
        screen.blit(self.img,(self.rect.x,self.rect.y))
        return action

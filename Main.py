import pygame
import os
import Button
from os import path
import time
import Chest
import random
import enemy
import Shop

ASSETS_FOLDER=os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER=os.path.join(ASSETS_FOLDER,'image_assets')

def show_chest_money(x,y,money_calc_display):
    money_calc_display_formatted=round(money_calc_display,2)
    money_calc_display_formatted="{:,}".format(money_calc_display_formatted)
    font=pygame.font.SysFont('calibri.ttf',16)
    money_calc_displayd=font.render('+$'+money_calc_display_formatted,True,(0,0,0))
    screen.blit(money_calc_displayd,(x,y))

def show_money(x,y,money):
    money_formatted=round(money,2)
    money_formatted="{:,}".format(money_formatted)
    font=pygame.font.SysFont('calibri.ttf',32)
    money_display=font.render('$'+money_formatted,True,(0,0,0))
    screen.blit(money_display,(x,y))

def show_hp(x,y,hp):
    font=pygame.font.SysFont('calibri.ttf',24)
    hp_display=font.render(str(hp)+'/'+str(max_hp),True,(0,0,0))
    screen.blit(hp_display,(x,y))

def player():
    if attacking==1 and atk_lock==0:
        if direction=='right':
            screen.blit(player_attacking_img_right,(playerX,playerY))
            player_width=player_attacking_img_right.get_width()
        else:
            screen.blit(player_attacking_img_left,(playerX-28,playerY))
            player_width=player_attacking_img_right.get_width()
    elif defending==1 and atk_lock==0:
        if direction=='right':
            screen.blit(player_defending_img_right,(playerX,playerY))
            player_width=player_defending_img_right.get_width()
        else:
            screen.blit(player_defending_img_left,(playerX-10,playerY))
            player_width=player_defending_img_left.get_width()
        
    else:
        screen.blit(player_img,(playerX,playerY))
        player_width=player_img.get_width()
    
def save(savedata):
    #print(savedata)
    if savedata['world']==-1:
        savedata['world']=savedata['worldsave']
    fp=open('savedata.txt', 'w+')
    for key in savedata:
        fp.write(str(key)+' '+str(savedata[key])+'\n')
    fp.close()

def saves(settings):
    #print(settings)
    fp=open('settings.txt','w+')
    for key in settings:
        fp.write(str(key)+' '+str(settings[key])+'\n')
    fp.close()

if path.exists('settings.txt'):
    temp_dict={}
    fp=open('settings.txt','r')
    for line in fp:
            line=line.strip()
            temp_list=line.split(' ')
            temp_dict[temp_list[0]]=float(temp_list[1])
    #print(temp_dict)
    Music=temp_dict['music']
    SFX=temp_dict['SFX']
    screenx=temp_dict['resolutionx']
    screeny=temp_dict['resolutiony']   
else:
    screenx=800
    screeny=screenx/(1920/1020)
scale=screenx/800
pygame.init()
screen=pygame.display.set_mode((screenx,screeny))

pygame.display.set_caption("Chest Jumper!")
icon=pygame.image.load(os.path.join(IMAGE_FOLDER, 'icon.png'))
pygame.display.set_icon(icon)
start_button_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'new_game.jpg'))
start_button_img=pygame.transform.scale(start_button_img,(300,150))
continue_button_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'continue_game.jpg'))
continue_button_img=pygame.transform.scale(continue_button_img,(300,150))
player_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'player.png'))
player_img=pygame.transform.scale(player_img,((player_img.get_width()*scale,(player_img.get_height()*scale))))
player_width=player_img.get_width()
player_height=player_img.get_height()
player_attacking_img_right=pygame.image.load(os.path.join(IMAGE_FOLDER, 'player_attacking_right.png'))
player_attacking_img_right=pygame.transform.scale(player_attacking_img_right,((player_attacking_img_right.get_width()*scale,(player_attacking_img_right.get_height()*scale))))
player_attacking_img_left=pygame.image.load(os.path.join(IMAGE_FOLDER, 'player_attacking_left.png'))
player_attacking_img_left=pygame.transform.scale(player_attacking_img_left,((player_attacking_img_left.get_width()*scale,(player_attacking_img_left.get_height()*scale))))
player_defending_img_left=pygame.image.load(os.path.join(IMAGE_FOLDER, 'player_defending_left.png'))
player_defending_img_left=pygame.transform.scale(player_defending_img_left,((player_defending_img_left.get_width()*scale,(player_defending_img_left.get_height()*scale))))
player_defending_img_right=pygame.image.load(os.path.join(IMAGE_FOLDER, 'player_defending_right.png'))
player_defending_img_right=pygame.transform.scale(player_defending_img_right,((player_defending_img_right.get_width()*scale,(player_defending_img_right.get_height()*scale))))
playerX=184*scale
playerY=368*scale
playerYconst=368*scale
RUNNING=True
world_check=0
world_save=1
savedata={}
settings_img=pygame.image.load(os.path.join(IMAGE_FOLDER,'settings-gears.png'))
settings_img=pygame.transform.scale(settings_img,((settings_img.get_width()*scale,(settings_img.get_height()*scale))))
settings_open=0
quit_img=pygame.image.load(os.path.join(IMAGE_FOLDER,'logout.png'))
quit_img=pygame.transform.scale(quit_img,((quit_img.get_width()*scale,(quit_img.get_height()*scale))))
SFX=1
Music=1
savedata_check=0          
settings_save={'music':Music,'SFX':SFX,'resolutionx':screenx,'resolutiony':screeny}
playerXchangea=0
playerXchanged=0
playerYchangew=0
playerYchanges=0
playerYchangecheck=0
savedy=0
falling=0
bonus=0
multi=1
money=0
hp=10
max_hp=10
atk=0
defense=0
bouncing=0
bounce_time=0
bounce_target=1
playerXchangealock=0
playerXchangedlock=0
bounce_movea=0
bounce_moved=0
world_left=0
world_right=0
money_calc_display=((1+bonus)*multi)
money_display_count=0
show_chest_money_timer_on=0
show_chest_money_timer=0
chesty=0
chestx=0
attacking=0
attacking_timer=0
atk_lock=0
attacking_cool=0
attacking_cool_timer=0
defending=0
direction='right'
enemy_cap=1
enemy_count=0
enemy_actions={}
atk_action3_timer=0
invincible_time=0
invincible=1
shop_data={'atk_base_boost':[0,60,60,20,'testingtestingtestingtesting'],'atk_multi_boost':[0,0,0,0,''],'chest_base_boost':[0,0,0,0,''],'chest_multi_boost':[0,0,0,0,''],'hp_pot':[0,0,0,0,'']}
buy_lock=0

while RUNNING:
    savedata={'world':world_check, 'worldsave':world_save, 'xpos':playerX,'ypos':playerY,'money':money,'hp':hp,'max_hp':max_hp,'atk':atk,'def':defense,'bonus':bonus,'multi':multi}
    if world_check==-1 and settings_open==0:
        world_check=world_save
    settings_button=Button.Button((screenx)-(64*scale),0,settings_img,scale)
    quit_button=Button.Button(768*scale,388*scale,quit_img,scale)
    start_button=Button.Button(50*scale,150*scale,start_button_img,scale)
    continue_button=Button.Button(450*scale,150*scale,continue_button_img,scale)
    #mouse_pos=pygame.mouse.get_pos()
    #print(mouse_pos)
    #print(screenx,screeny)
    
    if world_check==0:
        screen.fill((135,206,235))
        if quit_button.create(screen):
            if savedata_check!=0:
                save(savedata)
            saves(settings_save)
            pygame.quit()
        if start_button.create(screen):
            savedata={'world':1, 'worldsave':1, 'xpos':184*scale,'ypos':368*scale,'money':0,'hp':10,'max_hp':10,'atk':1,'def':1,'bonus':0,'multi':1}
            save(savedata)
            world_check=1
            savedata_check+=1
            playerX=savedata['xpos']*scale
            playerY=savedata['ypos']*scale
            money=savedata['money']
            hp=savedata['hp']
            max_hp=savedata['max_hp']
            atk=savedata['atk']
            defense=savedata['def']
            bonus=savedata['bonus']
            multi=savedata['multi']
            
        if continue_button.create(screen) and path.exists('savedata.txt'):
            fp=open('savedata.txt','r')
            for line in fp:
                line=line.strip()
                temp_list=line.split(' ')
                savedata[temp_list[0]]=float(temp_list[1])
            fp.close()
            savedata_check+=1
            if world_check==-1:
                world_check=savedata['worldsave']
            else:
                world_check=savedata['world']
            playerX=savedata['xpos']*scale
            playerY=savedata['ypos']*scale
            money=savedata['money']
            hp=savedata['hp']
            max_hp=savedata['max_hp']
            atk=savedata['atk']
            defense=savedata['def']
            bonus=savedata['bonus']
            multi=savedata['multi']
            #make sure to add in position being divided by scale when saving later
            if path.exists('shopdata.txt'):
                fp_shop=open('shopdata.txt','r')
                temp_list=[]
                for line in fp_shop:
                    line=line.strip()
                    temp_list.append(line)
                shop_data['atk_base_boost']=[int(temp_list[0]),60,60,20,'+1 to Base Attack']
                shop_data['atk_multi_boost']=[int(temp_list[1]),260,60,0,'+.1 to Attack Multiplier']
                shop_data['chest_base_boost']=[int(temp_list[2]),460,60,0,'+1 to Base Chest Gold']
                shop_data['chest_multi_boost']=[int(temp_list[3]),60,150,0,'+.1 to Chest Gold Multiplier']
                shop_data['hp_pot']=[int(temp_list[4]),60,240,100,'Consumable, heals 20 hp']
                #level, x, y, cost, description
                temp_list=[]
                fp_shop.close()
    elif world_check==-1:
        screen.fill((135,206,235))
    elif world_check==1:
        grass_floor_w1_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'grass_world1_floor.png'))
        grass_floor_w1_img=pygame.transform.scale(grass_floor_w1_img,((grass_floor_w1_img.get_width()*scale,(grass_floor_w1_img.get_height()*scale))))
        screen.blit(grass_floor_w1_img,(0,0))
        player()
        show_money(10,10,money)
        show_hp(10,30,hp)
        bouncy_chest=Chest.Chest(336,297,'chest.png',scale,bonus,multi)
        bouncy_chest_collision=bouncy_chest.create(screen,playerX,playerY,falling)
        if bouncy_chest_collision==1:
            playerXchangedlock=1
            playerXchangealock=0
        elif bouncy_chest_collision==2:
            playerXchangealock=1
            playerXchangedlock=0
        elif bouncy_chest_collision==3:
            bouncing=1
            playerXchangealock=0
            playerXchangedlock=0
        else:
            playerXchangealock=0
            playerXchangedlock=0
        if show_chest_money_timer==1 and show_chest_money_timer==0:
            chesty=278+random.randrange(-15,16)
            chestx=383+random.randrange(-15,16)
            show_chest_money_timer+=1
            #print('on')
        elif show_chest_money_timer_on==1 and 0<show_chest_money_timer<500:
            show_chest_money_timer+=1
            chesty+=.1
            show_chest_money(chestx,chesty,money_calc_display)
            #print(chestx,chesty)
        else:
            show_chest_money_timer_on=0
            show_chest_money_timer=0
        #print(show_chest_money_timer_on)
        world_left=2
        world_right=3
        #print(playerX,playerY)
    elif world_check==2:
        grass_floor_w1_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'grass_world1_floor.png'))
        grass_floor_w1_img=pygame.transform.scale(grass_floor_w1_img,((grass_floor_w1_img.get_width()*scale,(grass_floor_w1_img.get_height()*scale))))
        screen.blit(grass_floor_w1_img,(0,0))
        player()
        #[level (for consumables level = #owned),x,y,cost(add in function to increase cost with level later),desc]
        for key in shop_data:
            shop=Shop.shop_item(shop_data[key][1],shop_data[key][2],shop_data[key][0],shop_data[key][4],scale,shop_data[key][3])
            if shop.shop_spawn(screen):
                if money>=shop_data[key][3] and buy_lock==0:
                    shop_data[key][0]+=1
                    money-=shop_data[key][3]
                    buy_lock=1

        show_money(10,10,money)
        show_hp(10,30,hp)
        world_left=0
        world_right=1
        fp_shop=open('shopdata.txt','w+')
        for key in shop_data:
            fp_shop.write((str(shop_data[key][0]))+'\n')
        fp.close()

    elif world_check==3:
        grass_floor_w1_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'grass_world1_floor.png'))
        grass_floor_w1_img=pygame.transform.scale(grass_floor_w1_img,((grass_floor_w1_img.get_width()*scale,(grass_floor_w1_img.get_height()*scale))))
        screen.blit(grass_floor_w1_img,(0,0))
        player()

        if enemy_count==0:
            while enemy_cap>enemy_count:
                #[enemy type,x,y,hp,action lock, action lock timer,hit cooldown]
                probability=random.randrange(10)
                if probability<=9:
                    enemy_actions[enemy_count]=['goblin',750+random.randrange(11),368,10,0,0,0]
                    enemy_count+=1
                if probability==10:
                    enemy_actions[enemy_count]=['skeleton',random.randrange(1001),368,10,0,0,0]
        elif enemy_count>0:
            for key in enemy_actions:
                if enemy_actions[key][3]!=0:
                    #print(enemy_actions[key][1])
                    if enemy_actions[key][4]==1:
                        enemy_actions[key][5]+=1
                    if enemy_actions[key][5]==250:
                        enemy_actions[key][4]=0
                        enemy_actions[key][5]=0
                    if enemy_actions[key][0]=='goblin':
                        goblin=enemy.goblin(enemy_actions[key][1],enemy_actions[key][2],scale,playerX,playerY,player_width,player_height,attacking,defending,enemy_actions[key][4])
                        if goblin.spawn(screen)[0]==1:
                            #print('1')
                            enemy_actions[key][1]+=.2
                        elif goblin.spawn(screen)[0]==2:
                            #print('2')
                            enemy_actions[key][1]-=.2
                        #print(goblin.spawn(screen)[1])
                        #if goblin.spawn(screen)[1]==3:
                            #enemy_actions[key][4]=1
                        if goblin.spawn(screen)[1]==1 or goblin.spawn(screen)[1]==-2:
                            if invincible==0:
                                hp-=1
                                invincible=1
                            elif invincible_time==250:
                                invincible_time=0
                                invincible=0
                            else:
                                invincible_time+=1
                        if goblin.spawn(screen)[2] and enemy_actions[key][6]==0:
                            enemy_actions[key][3]-=1
                            print(enemy_actions[key][3])
                            enemy_actions[key][6]+=1
                        if enemy_actions[key][6]>0:
                            enemy_actions[key][6]+=1
                            if enemy_actions[key][6]>=300:
                                enemy_actions[key][6]=0
                        #print(enemy_actions[key][3])
                    if enemy_actions[key][3]==0:
                        money+=10
                        enemy_count-=1

        else:
            print('enemy count under 0')
        show_money(10,10,money)
        show_hp(10,30,hp)
        world_right=0
        world_left=1
    elif world_check==4:
        screen.fill((0,0,0))
        font=pygame.font.SysFont('calibri.ttf',72)
        hp_display=font.render("You Died",True,(255,255,255))
        screen.blit(hp_display,(300,100))
        continue_button_dead=Button.Button(260*scale,150*scale,continue_button_img,scale)
        if continue_button_dead.create(screen):
            world_check=1
            money=0
            world_check=1
            playerX=184*scale
            playerY=368*scale
            hp=1.0

    if world_check!=2:
        buy_lock=0
    if attacking==1 and atk_lock==0:
        if direction=='right':
            player_width=player_attacking_img_right.get_width()
        else:
            player_width=player_attacking_img_right.get_width()
    elif defending==1 and atk_lock==0:
        if direction=='right':
            player_width=player_defending_img_right.get_width()
        else:
            player_width=player_defending_img_left.get_width()
        
    else:
        player_width=player_img.get_width()
    if attacking_cool==1:
        atk_lock=1
        attacking_cool_timer+=1
        if attacking_cool_timer==200:
            atk_lock=0
            attacking_cool_timer=0
            attacking_cool=0

    elif attacking==1 and atk_lock==0 or defending==1 and atk_lock==0:
        attacking_timer+=1
        if attacking_timer==100:
            attacking=0
            defending=0
            attacking_timer=0
            attacking_cool=1
        
    if hp<=0:
        world_check=4

    if hp>max_hp:
        hp=max_hp

    if bouncing==1 and bounce_time==0:
        bounce_target=random.randrange(200,400)
        bounce_time+=playerYchangew
        money+=((1+bonus)*multi)/2
        if money_display_count<2 and show_chest_money_timer_on==0:
            money_display_count+=1
        else:
            show_chest_money_timer_on=1
            money_display_count=0
        bouncingXmovecoinflip=random.randrange(2)
        #print(bouncingXmovecoinflip)
        
        if bouncingXmovecoinflip==0:
            bounce_movea=(random.randrange(1,3))/10
            playerXchangea-=bounce_movea
            bounce_moved=0
            bounce_movea=1
        else:
            bounce_moved=(random.randrange(1,3))/10
            playerXchanged+=bounce_moved
            bounce_movea=0
            bounce_moved=1
    elif bounce_time>=bounce_target:
        bouncing=0
        bounce_time=0
        if bounce_movea==0:
            playerXchanged=0
        elif bounce_moved==0:
            playerXchangea=0
    elif bouncing==1 and bounce_time!=0:
        bounce_time+=playerYchangew
    elif bouncing==0:
        bounce_movea=0
        bounce_moved=0
    #print(bounce_time,bounce_target)
    playerY-=playerYchangew
    playerY-=playerYchanges
    playerYchangecheck=savedy-playerY
    if playerX>=788*scale:
        if world_right==0:
            playerXchanged=0
        else:
            world_check=world_right
            playerX=-15
    if playerX<=-16*scale:
        if world_left==0:
            playerXchangea=0
        else:
            world_check=world_left
            playerX=787
    if playerY>368*scale:
        playerYchanges=0
        playerY=368*scale
    if playerYchangecheck>=200*scale:
        playerYchangew=0
    elif bouncing==1:
        playerYchangew=.5
    elif playerY<368*scale:
        playerYchanges=-.3
    if playerY>=playerYconst:
        playerYchangecheck=0
        playerYchanges=0
    if playerYchangew!=0:
        if playerXchangealock==0:
            playerX+=playerXchangea*.5
        if playerXchangedlock==0:
            playerX+=playerXchanged*.5
    else:
        if playerXchangealock==0:
            playerX+=playerXchangea
        if playerXchangedlock==0:
            playerX+=playerXchanged
    if playerYchanges==0 and playerYchangew==0:
        savedy=playerY
        falling=0

    if settings_button.create(screen) or settings_open==1:
        if world_check!=-1 and world_check!=0:    
            world_save=world_check
        world_check=-1
        settings_menu_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'settings_menu.png'))
        settings_menu_img=pygame.transform.scale(settings_menu_img,((settings_menu_img.get_width()*scale,(settings_menu_img.get_height()*scale))))
        screen.blit(settings_menu_img,(100*scale,100*scale))
        settings_open=1
        menu_return_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'settings_return_menu.png'))
        menu_return_img=pygame.transform.scale(menu_return_img,((menu_return_img.get_width()*scale,(menu_return_img.get_height()*scale))))
        menu_return_button=Button.Button(250*scale,270*scale,menu_return_img,scale)
        settings_exit_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'settings_exit.png'))
        settings_exit_img=pygame.transform.scale(settings_exit_img,((settings_exit_img.get_width()*scale,(settings_exit_img.get_height()*scale))))
        settings_exit_button=Button.Button(670*scale,80*scale,settings_exit_img,scale)   
        if quit_button.create(screen):
            if savedata_check!=0:
                save(savedata)
            saves(settings_save)
            pygame.quit()
        if settings_save['SFX']==1:
            sfx_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'checked_box.png'))
            sfx_img=pygame.transform.scale(sfx_img,((sfx_img.get_width()*scale,(sfx_img.get_height()*scale))))
            
        else:
            sfx_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'unchecked_box.png'))
            sfx_img=pygame.transform.scale(sfx_img,((sfx_img.get_width()*scale,(sfx_img.get_height()*scale))))
        if settings_save['music']==1:
            music_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'checked_box2.png'))
            music_img=pygame.transform.scale(music_img,((music_img.get_width()*scale,(music_img.get_height()*scale))))
        else:
            music_img=pygame.image.load(os.path.join(IMAGE_FOLDER, 'unchecked_box2.png'))
            music_img=pygame.transform.scale(music_img,((music_img.get_width()*scale,(music_img.get_height()*scale))))
        sfx_button=Button.Button(230*scale,195*scale,sfx_img,scale)
        music_button=Button.Button(230*scale,240*scale,music_img,scale)
        x640=pygame.image.load(os.path.join(IMAGE_FOLDER, '640x480.png'))
        x640=pygame.transform.scale(x640,((x640.get_width()*scale,(x640.get_height()*scale))))
        x720=pygame.image.load(os.path.join(IMAGE_FOLDER, '1280x720.png'))
        x720=pygame.transform.scale(x720,((x720.get_width()*scale,(x720.get_height()*scale))))
        x1024=pygame.image.load(os.path.join(IMAGE_FOLDER, '1280x1024.png'))
        x1024=pygame.transform.scale(x1024,((x1024.get_width()*scale,(x1024.get_height()*scale))))
        x1920=pygame.image.load(os.path.join(IMAGE_FOLDER, '1920x1080.png'))
        x1920=pygame.transform.scale(x1920,((x1920.get_width()*scale,(x1920.get_height()*scale))))
        buttonx640=Button.Button(291*scale,148*scale,x640,scale)
        buttonx720=Button.Button(393*scale+(19*(scale-1)),148*scale,x720,scale)
        buttonx1024=Button.Button(498*scale+(19*(scale-1)),148*scale,x1024,scale)
        buttonx1920=Button.Button(602*scale+(19*(scale-1)),148*scale,x1920,scale)
        if buttonx640.create(screen):
            settings_save['resolutionx']=640
            settings_save['resolutiony']=640/(1920/1020)
            screenx=settings_save['resolutionx']
            screeny=settings_save['resolutiony']
            scale=screenx/800
            time.sleep(.1)
            screen=pygame.display.set_mode((screenx,screeny))
        if buttonx720.create(screen):
            settings_save['resolutionx']=800
            settings_save['resolutiony']=800/(1920/1020)
            screenx=settings_save['resolutionx']
            screeny=settings_save['resolutiony']
            scale=screenx/800
            time.sleep(.1)
            screen=pygame.display.set_mode((screenx,screeny))
        if buttonx1024.create(screen):
            settings_save['resolutionx']=1024
            settings_save['resolutiony']=1024/(1920/1020)
            screenx=settings_save['resolutionx']
            screeny=settings_save['resolutiony']
            scale=screenx/800
            time.sleep(.1)
            screen=pygame.display.set_mode((screenx,screeny))
        if buttonx1920.create(screen):
            settings_save['resolutionx']=1920
            settings_save['resolutiony']=1020
            screenx=settings_save['resolutionx']
            screeny=settings_save['resolutiony']
            scale=screenx/800
            time.sleep(.1)
            screen=pygame.display.set_mode((screenx,screeny))
        if music_button.create(screen):
            if settings_save['music']==1:
                settings_save['music']=0
                time.sleep(.1)
            else:
                settings_save['music']=1
                time.sleep(.1)
        if sfx_button.create(screen):
            if settings_save['SFX']==1:
                settings_save['SFX']=0
                time.sleep(.1)
            else:
                settings_save['SFX']=1
                time.sleep(.1)
        if settings_exit_button.create(screen):
            settings_open+=1
            world_check=world_save
        if menu_return_button.create(screen):
            if savedata_check!=0:
                save(savedata)
                print('saved')
                print(savedata)
            saves(settings_save)
            settings_open+=1
            world_check=0

    for event in pygame.event.get():
        if world_check>0 and event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and playerYchangecheck<250*scale and falling==0:
                playerYchangew=.8*scale
                #print(playerY)
            if event.key==pygame.K_a:
                playerXchangea=-.6*scale
                direction='left'
                #print(playerX)
                #print(playerY)
            if event.key==pygame.K_s and playerY<368*scale:
                playerYchanges=-.25*scale
                #print(playerY)
            if event.key==pygame.K_d:
                playerXchanged=.6*scale
                direction='right'
                #print(playerX)
        if world_check==3 and event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT:
                attacking=1
            if event.key==pygame.K_SPACE:
                defending=1
        if world_check==2 and event.type==pygame.MOUSEBUTTONUP:
            buy_lock=0
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                playerXchangea=0
            if event.key==pygame.K_d:
                playerXchanged=0
            if event.key==pygame.K_w:
                playerYchangew=0
                falling=1
            if event.key==pygame.K_s:
                playerYchanges=0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                settings_open=1
        if event.type==pygame.QUIT:
            if savedata_check!=0:
                save(savedata)
            saves(settings_save)
            RUNNING=False
            pygame.quit()
    #print(player_width)
    #print(savedata)
    pygame.display.update()

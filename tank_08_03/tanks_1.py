
import pygame
from nnet import *
from param import *
from prepareData import *
pygame.init()

#windowverture de la fenetre du jeu
window = pygame.display.set_mode((window_length, window_height))

pygame.display.set_caption("Deep Learning")

#Images
background = pygame.image.load('sprites/bg.png')
p_1 = pygame.image.load('sprites/p_1.png')
p_2 = pygame.image.load('sprites/p_2.png')


#Definition nnet
nb_input = 46
nb_hidden1 = 60
nb_hidden2 = 30
nb_hidden3 = 16
nb_output = 8

nb_tank = 3 
nnet_tab=[Nnet(nb_input, nb_hidden1, nb_hidden2, nb_hidden3, nb_output) for i in range(nb_tank)]
score_tab=[0 for i in range(nb_tank)]

playing_tank = 0
game_duration = 15000
time = 0

#Boucle principale
while game < game_max:

    input = data(x_p1,x_p2,y_p1,y_p2,life_p1,life_p2,bullets_p1,bullets_p2)
    output=nnet_tab[playing_tank].get_outputs(input)

    pygame.time.delay(delay)
    time += delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = game_max

    keys = pygame.key.get_pressed()

#Test des deplacements

    if output[0][0]>0.5 and x_p1>0:
        x_p1 -= speed

    if output[1][0]>0.5 and x_p1<window_length - width:
        x_p1 += speed

    if output[2][0]>0.5 and y_p1>0:
        y_p1 -= speed

    if output[3][0]>0.5 and y_p1< window_height - height:
        y_p1 += speed

    if keys[pygame.K_j] and x_p2>0:
        x_p2 -= speed

    if keys[pygame.K_l] and x_p2<window_length - width:
        x_p2 += speed

    if keys[pygame.K_i] and y_p2>0:
        y_p2 -= speed

    if keys[pygame.K_k] and y_p2< window_height - height:
        y_p2 += speed

# Test du tir du joueur 1

    if cooldown_p1 < 0:
        if output[4][0]>0.5 or output[5][0]>0.5 or output[6][0]>0.5 or output[7][0]>0.5 :
            i = 0
            while bullets_p1[i][0] :
                i += 1
            bullets_p1[i][0] = 1
            bullets_p1[i][1] = x_p1
            bullets_p1[i][2] = y_p1
            bullets_p1[i][3] = 0
            bullets_p1[i][4] = 0
            if output[4][0]>0.5 :
                bullets_p1[i][3] = -bullet_speed
            if output[5][0]>0.5 :
                bullets_p1[i][3] = bullet_speed
            if output[6][0]>0.5 :
                bullets_p1[i][4] = -bullet_speed
            if output[7][0]>0.5 :
                bullets_p1[i][4] = bullet_speed
            cooldown_p1 = cooldown_delay

    if cooldown_p1 >= 0:
        cooldown_p1 -= delay

#Test du tir du joueur 2

    if cooldown_p2 < 0:
        if keys[pygame.K_f] or keys[pygame.K_h] or keys[pygame.K_t] or keys[pygame.K_g]:
            i = 0
            while bullets_p2[i][0] :
                i += 1
            bullets_p2[i][0] = 1
            bullets_p2[i][1] = x_p2
            bullets_p2[i][2] = y_p2
            bullets_p2[i][3] = 0
            bullets_p2[i][4] = 0
            if keys[pygame.K_f]:
                bullets_p2[i][3] = -bullet_speed
            if keys[pygame.K_h]:
                bullets_p2[i][3] = bullet_speed
            if keys[pygame.K_t]:
                bullets_p2[i][4] = -bullet_speed
            if keys[pygame.K_g]:
                bullets_p2[i][4] = bullet_speed
            cooldown_p2 = cooldown_delay

    if cooldown_p2 >= 0:
        cooldown_p2 -= delay

#Affichages
    window.blit(background, (0,0))
    window.blit(p_1, (x_p1 - width/2, y_p1 - height/2, width, height))
    window.blit(p_2, (x_p2 - width/2, y_p2 - height/2, width, height))


# Bagarre et fin du jeu lorsqu'un des joueurs n'a plus de vie
    for i in range(max_bullet):
        if bullets_p1[i][0]:
            bullets_p1[i][1] += bullets_p1[i][3]
            bullets_p1[i][2] += bullets_p1[i][4]
            if abs(bullets_p1[i][1] - x_p2) < width and abs(bullets_p1[i][2] - y_p2) < height :
                bullets_p1[i] = [0 for j in range(5)]
                life_p2 -= 1
                if life_p2 == 0 :
                    game += 1
                    score = (life_p1-life_p2)/life_tot * (1 - time/game_duration)
                    print(score)
                    score_tab[playing_tank]=score
                    playing_tank = (playing_tank + 1) % nb_tank
                    life_p1 = life_tot
                    life_p2 = life_tot
                    x_p1 = 400
                    y_p1 = 400
                    x_p2 = 750
                    y_p2 = 400
                    bullets_p1 = [[0 for i in range(5)] for i in range(max_bullet)]
                    bullets_p2 = [[0 for i in range(5)] for i in range(max_bullet)]
                    time=0

            pygame.draw.circle(window, (255, 0, 0), (bullets_p1[i][1],bullets_p1[i][2]), bullet_radius, 0)
            if bullets_p1[i][1] > 800 or bullets_p1[i][1] < 0 or bullets_p1[i][2] > 800 or bullets_p1[i][2] < 0 :
                bullets_p1[i][0] = False

    for i in range(max_bullet):
        if bullets_p2[i][0]:
            bullets_p2[i][1] += bullets_p2[i][3]
            bullets_p2[i][2] += bullets_p2[i][4]
            if abs(bullets_p2[i][1] - x_p1) < width and abs(bullets_p2[i][2] - y_p1) < height :
                bullets_p2[i] = [0 for j in range(5)]
                life_p1 -= 1
                if life_p1 == 0 :
                    game += 1
                    score = (life_p1-life_p2)/life_tot * (1 - time/game_duration)
                    print(score)
                    score_tab[playing_tank]=score
                    playing_tank = (playing_tank + 1) % nb_tank
                    life_p1 = life_tot
                    life_p2 = life_tot
                    x_p1 = 400
                    y_p1 = 400
                    x_p2 = 750
                    y_p2 = 400
                    bullets_p1 = [[0 for i in range(5)] for i in range(max_bullet)]
                    bullets_p2 = [[0 for i in range(5)] for i in range(max_bullet)]
                    time=0

            pygame.draw.circle(window, (0, 255, 0), (bullets_p2[i][1],bullets_p2[i][2]), bullet_radius, 0)
            if bullets_p2[i][1] > 800 or bullets_p2[i][1] < 0 or bullets_p2[i][2] > 800 or bullets_p2[i][2] < 0 :
                bullets_p2[i][0] = False

    if time > game_duration :
        game += 1
        score = (life_p1-life_p2)/life_tot * (1 - time/game_duration)
        print(score)
        score_tab[playing_tank]=score
        playing_tank = (playing_tank + 1) % nb_tank
        life_p1 = life_tot
        life_p2 = life_tot
        x_p1 = 400
        y_p1 = 400
        x_p2 = 750
        y_p2 = 400
        bullets_p1 = [[0 for i in range(5)] for i in range(max_bullet)]
        bullets_p2 = [[0 for i in range(5)] for i in range(max_bullet)]
        time=0

    pygame.display.update()
pygame.quit()

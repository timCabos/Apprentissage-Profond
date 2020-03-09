
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

nb_tank = 5
nnet_tab1=[Nnet(nb_input, nb_hidden1, nb_hidden2, nb_hidden3, nb_output) for i in range(nb_tank)]
score_tab1=[0 for i in range(nb_tank)]

nnet_tab2=[Nnet(nb_input, nb_hidden1, nb_hidden2, nb_hidden3, nb_output) for i in range(nb_tank)]
score_tab2=[0 for i in range(nb_tank)]

playing_tank = 0
game_duration = 1500
time = 0

#Boucle principale
while game < game_max:

    input = data(x_p1,x_p2,y_p1,y_p2,life_p1,life_p2,bullets_p1,bullets_p2)
    output1=nnet_tab1[playing_tank].get_outputs(input)
    output2=nnet_tab2[playing_tank].get_outputs(input)

    pygame.time.delay(delay)
    time += delay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = game_max

    keys = pygame.key.get_pressed()

#Test des deplacements

    if output1[0][0]>0.5 and x_p1>0:
        x_p1 -= speed

    if output1[1][0]>0.5 and x_p1<window_length - width:
        x_p1 += speed

    if output1[2][0]>0.5 and y_p1>0:
        y_p1 -= speed

    if output1[3][0]>0.5 and y_p1< window_height - height:
        y_p1 += speed

    if output2[0][0]>0.5 and x_p2>0:
        x_p2 -= speed

    if output2[1][0]>0.5 and x_p2<window_length - width:
        x_p2 += speed

    if output2[2][0]>0.5 and y_p2>0:
        y_p2 -= speed

    if output2[3][0]>0.5 and y_p2< window_height - height:
        y_p2 += speed

# Test du tir du joueur 1

    if cooldown_p1 < 0:
        if output1[4][0]>0.5 or output1[5][0]>0.5 or output1[6][0]>0.5 or output1[7][0]>0.5 :
            i = 0
            while bullets_p1[i][0] :
                i += 1
            bullets_p1[i][0] = 1
            bullets_p1[i][1] = x_p1
            bullets_p1[i][2] = y_p1
            bullets_p1[i][3] = 0
            bullets_p1[i][4] = 0
            if output1[4][0]>0.5 :
                bullets_p1[i][3] = -bullet_speed
            if output1[5][0]>0.5 :
                bullets_p1[i][3] = bullet_speed
            if output1[6][0]>0.5 :
                bullets_p1[i][4] = -bullet_speed
            if output1[7][0]>0.5 :
                bullets_p1[i][4] = bullet_speed
            cooldown_p1 = cooldown_delay

    if cooldown_p1 >= 0:
        cooldown_p1 -= delay

#Test du tir du joueur 2

    if cooldown_p2 < 0:
        if output2[4][0]>0.5 or output2[5][0]>0.5 or output2[6][0]>0.5 or output2[7][0]>0.5 :
            i = 0
            while bullets_p2[i][0] :
                i += 1
            bullets_p2[i][0] = 1
            bullets_p2[i][1] = x_p2
            bullets_p2[i][2] = y_p2
            bullets_p2[i][3] = 0
            bullets_p2[i][4] = 0
            if output2[4][0]>0.5 :
                bullets_p2[i][3] = -bullet_speed
            if output2[5][0]>0.5 :
                bullets_p2[i][3] = bullet_speed
            if output2[6][0]>0.5 :
                bullets_p2[i][4] = -bullet_speed
            if output2[7][0]>0.5 :
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
                    score = (life_p1-life_p2)/life_tot * (1 - time/(2*game_duration))
                    print(score)
                    score_tab1[playing_tank]=score
                    score_tab2[playing_tank]=-score
                    playing_tank = (playing_tank + 1)
                    life_p1 = life_tot
                    life_p2 = life_tot
                    x_p1 = 200
                    y_p1 = 300
                    x_p2 = 600
                    y_p2 = 500
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
                    score = (life_p1-life_p2)/life_tot * (1 - time/(2*game_duration))
                    print(score)
                    score_tab1[playing_tank]=score
                    score_tab2[playing_tank]=-score
                    playing_tank = (playing_tank + 1)
                    life_p1 = life_tot
                    life_p2 = life_tot
                    x_p1 = 200
                    y_p1 = 300
                    x_p2 = 600
                    y_p2 = 500
                    bullets_p1 = [[0 for i in range(5)] for i in range(max_bullet)]
                    bullets_p2 = [[0 for i in range(5)] for i in range(max_bullet)]
                    time=0

            pygame.draw.circle(window, (0, 255, 0), (bullets_p2[i][1],bullets_p2[i][2]), bullet_radius, 0)
            if bullets_p2[i][1] > 800 or bullets_p2[i][1] < 0 or bullets_p2[i][2] > 800 or bullets_p2[i][2] < 0 :
                bullets_p2[i][0] = False

    if time > game_duration :
        game += 1
        score = (life_p1-life_p2)/life_tot * (1 - time/(2*game_duration))
        print(score)
        score_tab1[playing_tank]=score
        score_tab2[playing_tank]=-score
        playing_tank = (playing_tank + 1)
        life_p1 = life_tot
        life_p2 = life_tot
        x_p1 = 200
        y_p1 = 300
        x_p2 = 600
        y_p2 = 500
        bullets_p1 = [[0 for i in range(5)] for i in range(max_bullet)]
        bullets_p2 = [[0 for i in range(5)] for i in range(max_bullet)]
        time=0

    if playing_tank == nb_tank :
        playing_tank = 0
        print(score_tab1)
        good_nn1, bad_nn1 = darwin(nnet_tab1, score_tab1)
        good_nn2, bad_nn2 = darwin(nnet_tab2, score_tab2)
        bad_nn1 = sort_bad(bad_nn1)
        bad_nn2 = sort_bad(bad_nn2)
        child1 = breed(good_nn1[0], good_nn1[1])
        child2 = breed(good_nn2[0], good_nn2[1])
        nnet_tab1 = [good_nn1[0], good_nn1[1], bad_nn1[0], bad_nn1[1], child1]
        nnet_tab2 = [good_nn2[0], good_nn2[1], bad_nn2[0], bad_nn2[1], child2]
        random.shuffle(nnet_tab1)
    pygame.display.update()
pygame.quit()

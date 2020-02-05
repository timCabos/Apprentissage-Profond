#Imports

import pygame
import scipy
pygame.init()

#Ouverture de la fenètre du jeu

window = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Deep Learning")

#Paramètres du jeu

run = True                                                      #Jeu en cours

delay = 20                                                      #Pas de temps du jeu (en ms)
radius = 16                                                     #Rayon du personnage
speed = 4                                                       #Vitesse du personnage
cooldown_delay = 500                                            #Temps de rechargement (en ms)
cooldown = 0                                                    #Disponibilité du tir
max_bullet = 10                                                 #Nombre maximum de tirs
bullets = [[0 for i in range(5)] for i in range(max_bullet)]    #Tableau des tirs émis : (Exist?, x, y, x_speed, y_speed)
bullet_speed = 12                                               #Vitesse des tirs
bullet_radius = 4

#Position initiale du joueur
x = 400
y = 400

#Boucle principale

while run:

    pygame.time.delay(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

#Test des déplacements

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed

#Test du tir

    if cooldown < 0:
        if keys[pygame.K_q] or keys[pygame.K_d] or keys[pygame.K_z] or keys[pygame.K_s]:
            i = 0
            while bullets[i][0] :
                i += 1
            bullets[i][0] = 1
            bullets[i][1] = x
            bullets[i][2] = y
            bullets[i][3] = 0
            bullets[i][4] = 0
            if keys[pygame.K_q]:
                bullets[i][3] = -bullet_speed
            if keys[pygame.K_d]:
                bullets[i][3] = bullet_speed
            if keys[pygame.K_z]:
                bullets[i][4] = -bullet_speed
            if keys[pygame.K_s]:
                bullets[i][4] = bullet_speed
            cooldown = cooldown_delay

    if cooldown >= 0:
        cooldown -= delay


#Affichages

    window.fill((100,100,200))

    pygame.draw.circle(window, (255,150,200), (x, y), radius, 0)

    for i in range(max_bullet):
        if bullets[i][0]:
            bullets[i][1] += bullets[i][3]
            bullets[i][2] += bullets[i][4]
            pygame.draw.circle(window, (255, 0, 0), (bullets[i][1],bullets[i][2]), bullet_radius, 0)
            if bullets[i][1] > 800 or bullets[i][1] < 0 or bullets[i][2] > 800 or bullets[i][2] < 0 :
                bullets[i][0] = False

    pygame.display.update()

pygame.quit()

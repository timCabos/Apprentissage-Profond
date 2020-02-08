
import pygame
pygame.init()

#windowdowverture de la fenetre du jeu

windowdow = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Deep Learning")

#Images

largeur = 65
hauteur = 65

background = pygame.image.load('sprites/bg.png')
p_1 = pygame.image.load('sprites/p_1.png')
p_2 = pygame.image.load('sprites/p_2.png')

#Parametres du jeu

run = True                                                      #Jeu en cours
delay = 20                                                      #Pas de temps du jeu (en ms)
radius = 16                                                     #Rayon du personnage
speed = 4                                                       #Vitesse du personnage
cooldown_delay = 500                                            #Temps de rechargement (en ms)
cooldown_p1 = 0                                                 #Disponibilite du tir
cooldown_p2 = 0
max_bullet = 10                                                 #Nombre maximum de tirs
bullets_p1 = [[0 for i in range(5)] for i in range(max_bullet)]  #Tableau des tirs emis : (Exist?, x, y, x_speed, y_speed)
bullets_p2 = [[0 for i in range(5)] for i in range(max_bullet)]
bullet_speed = 12                                               #Vitesse des tirs
bullet_radius = 4

#Position initiale des joueurs
x_p1 = 50
y_p1 = 400
x_p2 = 750
y_p2 = 400
#Boucle principale

while run:

    pygame.time.delay(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

#Test des deplacements

    if keys[pygame.K_LEFT]:
        x_p1 -= speed

    if keys[pygame.K_RIGHT]:
        x_p1 += speed

    if keys[pygame.K_UP]:
        y_p1 -= speed

    if keys[pygame.K_DOWN]:
        y_p1 += speed

    if keys[pygame.K_j]:
        x_p2 -= speed

    if keys[pygame.K_l]:
        x_p2 += speed

    if keys[pygame.K_i]:
        y_p2 -= speed

    if keys[pygame.K_k]:
        y_p2 += speed

#Test du tir du joueur 1

    if cooldown_p1 < 0:
        if keys[pygame.K_q] or keys[pygame.K_d] or keys[pygame.K_z] or keys[pygame.K_s]:
            i = 0
            while bullets_p1[i][0] :
                i += 1
            bullets_p1[i][0] = 1
            bullets_p1[i][1] = x_p1
            bullets_p1[i][2] = y_p1
            bullets_p1[i][3] = 0
            bullets_p1[i][4] = 0
            if keys[pygame.K_q]:
                bullets_p1[i][3] = -bullet_speed
            if keys[pygame.K_d]:
                bullets_p1[i][3] = bullet_speed
            if keys[pygame.K_z]:
                bullets_p1[i][4] = -bullet_speed
            if keys[pygame.K_s]:
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
    windowdow.blit(background, (0,0))
    windowdow.blit(p_1, (x_p1, y_p1, largeur, hauteur))
    windowdow.blit(p_2, (x_p2, y_p2, largeur, hauteur))

    for i in range(max_bullet):
        if bullets_p1[i][0]:
            bullets_p1[i][1] += bullets_p1[i][3]
            bullets_p1[i][2] += bullets_p1[i][4]
            pygame.draw.circle(windowdow, (255, 0, 0), (bullets_p1[i][1],bullets_p1[i][2]), bullet_radius, 0)
            if bullets_p1[i][1] > 800 or bullets_p1[i][1] < 0 or bullets_p1[i][2] > 800 or bullets_p1[i][2] < 0 :
                bullets_p1[i][0] = False

    for i in range(max_bullet):
        if bullets_p2[i][0]:
            bullets_p2[i][1] += bullets_p2[i][3]
            bullets_p2[i][2] += bullets_p2[i][4]
            pygame.draw.circle(windowdow, (0, 255, 0), (bullets_p2[i][1],bullets_p2[i][2]), bullet_radius, 0)
            if bullets_p2[i][1] > 800 or bullets_p2[i][1] < 0 or bullets_p2[i][2] > 800 or bullets_p2[i][2] < 0 :
                bullets_p2[i][0] = False

    pygame.display.update()

pygame.quit()

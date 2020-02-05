import pygame as pg
pg.init()

Lx=500
Ly=500
win = pg.display.set_mode((Lx,Ly))
pg.display.set_caption("Jeu en Python")

background = pg.image.load('sprites/bg.png')
p_1 = pg.image.load('sprites/p_1.png')
p_2 = pg.image.load('sprites/p_2.png')


x_p1 = 50
y_p1 = 250
x_p2 = 450
y_p2 = 250
largeur = 65
hauteur = 65
vitesse = 4

run=True
while run :
    pg.time.delay(25)

    for event in pg.event.get() :
        if event.type == pg.QUIT :
            run= False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x_p1 > vitesse :
        x_p1 -= vitesse
    if keys [pg.K_RIGHT] and x_p1 < Lx -largeur -vitesse :
        x_p1 += vitesse
    if keys[pg.K_UP] and y_p1 > vitesse :
        y_p1 -= vitesse
    if keys [pg.K_DOWN] and y_p1 < Ly -largeur -vitesse :
        y_p1 += vitesse


    if keys[pg.K_a] and x_p2 > vitesse :
        x_p2 -= vitesse
    if keys [pg.K_d] and x_p2 < Lx -largeur -vitesse :
        x_p2 += vitesse
    if keys[pg.K_w] and y_p2 > vitesse :
        y_p2 -= vitesse
    if keys [pg.K_s] and y_p2 < Ly -largeur -vitesse :
        y_p2 += vitesse

    win.blit(background, (0,0))
    win.blit(p_1, (x_p1, y_p1, largeur, hauteur))
    win.blit(p_2, (x_p2, y_p2, largeur, hauteur))

    pg.display.update()
pg.quit()

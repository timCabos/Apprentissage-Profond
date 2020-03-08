#parametres Jeu
window_height = 800
window_length = 800
width = 65
height = 65

#run = True                                                      #Jeu en cours
game_max = 10                                                    #nombre de parties qui seront jouees
game = 0                                                        #nombre de parties jouees
delay = 20                                                      #Pas de temps du jeu (en ms)
radius = 16                                                     #Rayon du personnage
speed = 6                                                       #Vitesse du personnage
cooldown_delay = 300                                            #Temps de rechargement (en ms)
cooldown_p1 = 0                                                 #Disponibilite du tir
cooldown_p2 = 0
max_bullet = 4                                                #Nombre maximum de tirs
bullets_p1 = [[0 for i in range(5)] for i in range(max_bullet)]  #Tableau des tirs emis : (Exist?, x, y, x_speed, y_speed)
bullets_p2 = [[0 for i in range(5)] for i in range(max_bullet)]
bullet_speed = 15                                               #Vitesse des tirs
bullet_radius = 4
life_tot = 3
life_p1 = life_tot
life_p2 = life_tot

#Position initiale des joueurs
x_p1 = 400
y_p1 = 400
x_p2 = 750
y_p2 = 400

# Paramètre NN

activ=0.5
mutation_chance = 0.2

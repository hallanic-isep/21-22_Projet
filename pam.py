import random

def create_model():

    root = {}

    # Nombre initial de points de vie
    root["live_points"] = 10 # équivalent à "live_points = 10" mais peut être stocké sur fichier

    labyrinth = [] # Liste de ligne (vide au départ)
    for line_n in range(4):
        rooms_line = []
        for room_n in range(4):
            # Contenu de la salle
            room = {}
            room["content"] = "." # . pour indiquer que la salle est vide
            room["visited"] = False
            # Ajout de la salle à la ligne
            rooms_line.append(room)
            #print("rooms_line",rooms_line)
        # Ajout de la ligne complète au labyrinthe
        labyrinth.append(rooms_line)
        #print("labyrinth", labyrinth)
    root["labyrinth"] = labyrinth

    # Ajout des éléments du jeu dans les salles
    shuffle_li = [0,1,2,3]
    shuffle_co = [0,1,2,3]
    random.shuffle(shuffle_li)
    random.shuffle(shuffle_co)
    print(shuffle_li,shuffle_co)
    # Initialisation des positions
    # ATTENTION ! CETTE PARTIE EST COMPLEXE...
    root["labyrinth"][ shuffle_li[0] ][ shuffle_co[0] ]["content"] = "J"
    root["labyrinth"][ shuffle_li[0] ][ shuffle_co[0] ]["visited"] = True
    root["labyrinth"][ shuffle_li[1] ][ shuffle_co[1] ]["content"] = "D"
    root["labyrinth"][ shuffle_li[2] ][ shuffle_co[2] ]["content"] = "T"
    # ... décomposition de la ligne ci dessus :
    # dictionaire du modèle de donnée
    #   -> clé "labyrinth"
    #       -> liste des lignes
    #           -> case entre 0 et 3 dans la liste des lignes
    #               -> liste des salles d'une ligne
    #                   -> case entre 0 et 3 dans la liste des salles
    #                       -> dictionaire d'une salle
    #                           -> clé "content"
    #                               -> on y associe la valeur "T"

    #print("root",root)
    return root
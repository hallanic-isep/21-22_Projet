def print_model( data ):

    print("POINTS DE VIE =", data["live_points"])

    for line in data["labyrinth"]:
        for room in line:
            if room["visited"]:
                print(room["content"],end="") # On reste sur la même ligne
            else:
                print("#",end="") # Piece non visitée
        print() # Passage à la line suivante

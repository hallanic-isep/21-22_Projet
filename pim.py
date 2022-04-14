import pam
import poum
def start_game():
    print("Bienvenue dans notre jeu de \"Donjon & Dragon\"")
    model = pam.create_model()
    #print("model",model)
    poum.print_model( model )
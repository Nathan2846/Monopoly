import classes

def init():
    print ('Welcome to Monopoly!')

    #Get number of players
    num_players = int(input('How many players will be playing?'))
    player_list = []

    #Create each player
    for i in range(num_players):
        #'__name', '__number','__money','__properties', '__position'
        #Get the name for each player and create them
        name = input('What is player ' + str(i+1) + '\'s name?')
        player = classes.Player(i +1, name)

        #Add each to the player list
        player_list.append(player)
    
    #Create the game
    game= classes.Game(player_list)

    #Ready to play
    return game

def main():
    game = init()


if __name__ == "__main__":
    main()

    
import classes

SPECIAL = ['Chance','Community Chest','Go','Jail','Income Tax','Free Parking','Go To Jail','Luxury tax']
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
    return game, player_list

def take_turn(player, game,player_list):
    #Set variables
    roll_number = 0
    print(f'{player.get_name()}, your up!')

    while True:
        #Roll 
        input (f'Press enter to roll! This is roll number {roll_number}')
        roll = game.roll_dice
        roll_number +=1 

        #Check for 3 rounds of doubles, otherwise move
        if roll[1] and roll_number == 3:
            #Go to Jail!
            break

        # Get the space
        print (f'You move {roll[0]} spaces!')
        player.move_spaces(roll[0])
        space = game.get_space(player.get_position())
        space_attributes = space.get_attributes()
        # Announce the space
        print(f"You have landed on {space_attributes[0]}")

        # Take action
        if space[0] in SPECIAL:
            #Do something special 
            pass
        else:
            #It's a property
            if space.check_ownership(player.get_name()):
                #We own this - take no action
                input ('You already own this property - press enter to continue')
            elif space.check_ownership(None):
                #No one owns this - it can be bought
                print ('This space is not owned - you have the option to buy it')
                print (f'You have {player.get_money()} dollars')
                print (f'The property costs {space_attributes[1]} dollars')
                if player.get_money() < space_attributes[1]:
                    #Insufficient funds
                    input('You do not have enough money to buy this space - press enter to continue')
                else:
                    purchase = input('Press 1 to buy this space, and press any other key to pass:')
                    if purchase == '1':
                        #Player buys the property
                        space.assign_owner(player.get_name())
                        player.add_money(-1 * space_attributes[2])
                        print (f'Property purchased - you now have {player.get_money()} dollars')
            else:
                #The property belongs to someone else
                owner = space.get_owner()
                rent = space.get_rent()
                print(f'This space is owned by {owner} and has a rent value of {rent}')
                print (f'You have {player.get_money()} now and will have {player.get_money() - rent} after the transaction')
                input ('Press enter to continue')
                if rent > player.get_money():
                    # Insufficient funds - call function
                    pass
                player.add_money(-1 * rent)

                #Find owner 
                for i in range (len(player_list)):
                    if player_list[i].get_name() == owner:
                        player_list[i].add_money(rent)
                        break


def main():
    game, player_list = init()


if __name__ == "__main__":
    main()

    
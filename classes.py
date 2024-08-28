import random 

class Space:
    __slots__ = ['__current_house','__name','__cost','__rent','__onehouse','__twohouse','__threehouse','__fourhouse','__hotel','__mortgage', '__owner', '__house_cost']

    def __init__(self, name, cost, rent, onehouse, twohouse, threehouse, fourhouse, hotel, house_cost):
        self.__name, self.__cost,self. __rent, self.__onehouse, self.__twohouse, self.__threehouse, self.__fourhouse, self.__hotel, self.__house_cost = name, cost, rent, onehouse, twohouse, threehouse, fourhouse, hotel, house_cost
        self.__owner = None
        self.__current_house = 0

    def get_attributes(self):
        result = [self.__name, self.__cost, self.__rent, self.__onehouse, self.__twohouse, self.__threehouse, self.__fourhouse, self.__hotel, self.__owner, self.__house_cost]
        return result
    
    def assign_owner(self, owner):
        self.__owner = owner

    def check_ownership(self, player_to_check):
        if player_to_check.get_name() == self.__owner:
            return True
        return False
    def purchase_house(self):
        self.__current_house += 1

class Player:
    __slots__  = ['__name', '__number','__money','__properties', '__position']

    def __init__(self, name, number):
        self.__name, self.__number = name, number
        self.__money = 1500
        self.__propertes = []
        self.__position = 0
    def get_name(self):
        return self.__name
    def add_money(self, amount):
        self.__money += amount
        return self.__money
    def move_spaces(self, spaces):
        self.__position += spaces

        if self.__position > 39:
            self.__position -=40
        return self.__position

class Game:
    __slots__ = ['__board', '__players', '__chance','__cc']

    def __init__(self, player_list):
        self.__players = player_list
   

        #Create all the properties
        board = []
        board.append(Space('Mediterranean Avenue',60,2,10,30,90,160,250,50))
        board.append(Space('Community Chest',0,0,0,0,0,0,0,0))
        board.append(Space('Baltic Avenue',60,4,20,60,180,320,450,50))
        board.append(Space('Income Tax',0,200,0,0,0,0,0,0))
        board.append(Space('Reading RR',200,25,25,50,100,200,0,0))
        board.append(Space('Oriental Avenue',100,6,30,90,270,400,550,50))
        board.append(Space('Chance',0,0,0,0,0,0,0,0))
        board.append(Space('Vermont Avenue',100,6,30,90,270,400,550,50))
        board.append(Space('Conneticut Avenue',120,8,40,100,300,450,600,50))
        board.append(Space('Jail',0,0,0,0,0,0,0,0))

        board.append(Space('St. Charles Place', 140,10,50,150,450,625,750,100))
        board.append(Space('Electric Company',150,0,0,0,0,0,0,0))
        board.append(Space('States Avenue', 140,10,50,150,450,625,750,100))
        board.append(Space('Virginia Avenue',160,12,60,180,500,700,900,100))
        board.append(Space('Pennsylvania RR',200,25,25,50,100,200,0,0))
        board.append(Space('St. James Place',180,14,70,200,550,750,950,100))
        board.append(Space('Community Chest',0,0,0,0,0,0,0,0))
        board.append(Space('Tennesse Avenue',180,14,70,200,550,750,950,100))
        board.append(Space('New York Avenue',200,16,80,220,600,800,1000))
        board.append(Space('Free Parking',0,0,0,0,0,0,0,0))

        board.append(Space('Kentucky Avenue',220,18,90,250,700,875,1050,150))
        board.append(Space('Chance',0,0,0,0,0,0,0,0))
        board.append(Space('Indiana Avenue',220,18,90,250,700,875,1050,150))
        board.append(Space('Illinois Avenue',240,20,100,300,750,925,1100,150))
        board.append(Space('B&O Railroad',200,25,25,50,100,200,0,0))
        board.append(Space('Atlantic Avenue',260,22,110,330,800,975,1150,150))
        board.append(Space('Ventnor Avenue',260,22,110,330,800,975,1150,150))
        board.append(Space('water Works',150,0,0,0,0,0,0,0))
        board.append(Space('Marvin Gardens',280,24,120,360,850,1025,1200,150))
        board.append(Space('Go To Jail',0,0,0,0,0,0,0,0))

        board.append(Space('Pacific Avenue',300,26,130,390,900,1100,1275,200))
        board.append(Space('North Carolina Avenue',300,26,130,390,900,1100,1275,200))
        board.append(Space('Community Chest',0,0,0,0,0,0,0,0))
        board.append(Space('Pennsylvania Avenue',320,28,150,450,1000,1200,1400,200))
        board.append(Space('Short Line',200,25,25,50,100,200,0,0))
        board.append(Space('Chance',0,0,0,0,0,0,0,0))
        board.append(Space('Park Place',350,35,175,500,1100,1300,1500,200))
        board.append(Space('Luxury Tax',0,100,0,0,0,0,0,0))
        board.append(Space('Boardwalk',400,50,200,600,1400,1700,2000,200))
    
        #Make the board the board
        self.__board = board

        #Create Chance
        chance = []
        chance.append({'refcode':1, 'message':'Advance to Boardwalk'})
        chance.append({'refcode':2, 'message':'Advance to Go (Collect $200)'})
        chance.append({'refcode':3, 'message':'Advance to Illionois Avenue. If you pass Go,  collect $200'})
        chance.append({'refcode':4,'message':'Advance to St. Charles Place. If you pass Go, collect $200'})
        chance.append({'refcode':5,'message':'Advance to the nearest Railroad. If unowned, you may buy it from the bank. If owned, pay owner twice the rent which they are otherwise entitled.'})
        chance.append({'refcode':6,'message':'Advance to the nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total tem times the amount shown'})
        chance.append({'refcode':7,'message':'Bank pays you dividend of $50'})
        chance.append({'refcode':8,'message':'Get Out of Jail Free'})
        chance.append({'refcode':9,'message':'Go Back 3 spaces'})
        chance.append({'refcode':10,'message':'Got to Jail.  Go directly to Jail, do not pass Go, do not collect $200'})
        chance.append({'refcode':11,'message':'Make general repairs on all your property. For each ouse pay $25. For each hotel, pay $100'})
        chance.append({'refcode':12,'message':'Speeding fine $15'})
        chance.append({'refcode':13,'message':'Take a trip to reading railroad. If you pass Go, collect $200'})
        chance.append({'refcode':14,'message':'You have been elected chairman of the board. Pay each player %50'})
        chance.append({'refcode':15,'message':'Your building loan matures. Collect $50'})
        self.__chance = chance

        #Create community chest
        cc = []
        cc.append({'refcode':1,'message':'Advance to Go (Collect $200)'})
        cc.append({'refcode':2,'message':'Bank error in your favor. Collect $200'})
        cc.append({'refcode':3,'message':'Doctor\'s fee. Pay $50'})
        cc.append({'refcode':4,'message':'From sale of stock you get $50'})
        cc.append({'refcode':5,'message':'Get Out Of Jail Free'})
        cc.append({'refcode':6,'message':'Go to Jail. Go directly to jail, do not pass go, do not collect $200'})
        cc.append({'refcode':7,'message':'Holiday fun matures. Recceive $100'})
        cc.append({'refcode':8,'message':'Income tax refund. Collect $20'})
        cc.append({'refcode':9,'message':'It is your birthday. Collect $10 from every player'})
        cc.append({'refcode':10,'message':'Life insurance matures. Collect $100'})
        cc.append({'refcode':11,'message':'Pay hospital fees of $100'})
        cc.append({'refcode':12,'message':'Pay school fees of $50'})
        cc.append({'refcode':13,'message':'Recceive $25 consultancy fee'})
        cc.append({'refcode':14,'message':'You are assessed for street repair. $40 per house, %115 per hotel'})
        cc.append({'refcode':15,'message':'You have won second prize in a beauty contest. Collect $10'})
        cc.append({'refcode':16,'message':'You inherit $100'})
        self.__cc = cc

        #Shuffle both decks
        random.shuffle(self.__cc)
        random.shuffle(self.__chance)

    def remove_chance_goojf(self):
        for i in range(len(self.__chance)):
            if self.__chance[i]['refcode'] == 8:
                self.__chance.pop(i)
                return True
        return False
    
    def remove_cc_goojf(self):
        for i in range(len(self.__cc)):
            if self.__cc[i]['refcode'] == 5:
                self.__cc.pop(i)
                return True
        return False
    
    def add_chance_goojf(self):
        self.__chance.append({'refcode':8,'message':'Get Out of Jail Free'})

    def add_cc_goojf(self):
        self.__cc.append({'refcode':5,'message':'Get Out of Jail Free'})


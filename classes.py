class Space:
    __slots__ = ['__name','__cost','__rent','__onehouse','__twohouse','__threehouse','__fourhouse','__hotel','__mortgage', '__owner', '__house_cost']

    def __init__(self, name, cost, rent, onehouse, twohouse, threehouse, fourhouse, hotel, house_cost):
        self.__name, self.__cost,self. __rent, self.__onehouse, self.__twohouse, self.__threehouse, self.__fourhouse, self.__hotel, self.__house_cost = name, cost, rent, onehouse, twohouse, threehouse, fourhouse, hotel, house_cost
        self.__owner = None

    def get_attributes(self):
        result = [self.__name, self.__cost, self.__rent, self.__onehouse, self.__twohouse, self.__threehouse, self.__fourhouse, self.__hotel, self.__owner, self.__house_cost]
        return result
    
    def assign_owner(self, owner):
        self.__owner = owner

    def check_ownership(self, player_to_check):
        if player_to_check.get_name() == self.__owner:
            return True
        return False

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
    __slots__ = ['__board', '__players', '__chance','__community_chest']

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



    
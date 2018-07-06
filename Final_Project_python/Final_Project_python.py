#PIC 10C Final Project: Learning Python 

#import cards

import random          #random library

''' The class card randomly generats cards 2-10, Jack, Queen, King, Ace with
suits spades, clubs, hearts, and diamonds.
'''
class card:

    suit = " "
    rank = 0

    #prints out rank and suit of card
    def print_card(self):                   
        print("          %d of %s" % (self.rank, self.suit))          #string formatting different than cout

    #overload < operator
    def __lt__(self,other):               
       return (self.rank < other.rank)
    
   #sets values to each rank and randomly generates cards
    def set_values(self):
        r1 = random.randrange(1,13)       #chooses random number correlating to type of card in deck
        set_rank = {                 #have to use a dictionary list in python instead of switch function
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10,
            11: 10,
            12: 10,
            13: 13,
        } 
        self.rank = set_rank[r1]           #change the value of rank
        r2 = random.randrange(1,4)      #chooses a random number correlating to suit of card in deck
        set_suit = {
            1: "spades",
            2: "clubs",
            3: "hearts",
            4: "diamonds",
        } 
        self.suit = set_suit[r2]            #change the value of suit

''' The class hand stores the player's cards and prints it out.
'''
class hand:

    def __init__(self, name):
        self.name = name
        self.player_hand = []
        self.total = 0
    
    #adds a new card to the player's hand and keeps track of the total value
    def add_card(self, card):
        self.player_hand.append(card)
        self.total = self.total + card.rank
    
    #prints all the cards in the hand
    def print_hand(self):
        for x in self.player_hand:           #for loop that iterates through the list
            x.print_card()

''' The player hand stores the player's money.
'''
class player: 
    money = 0

    #set buy in amount
    def buy_in(self, start_money):
        self.money = start_money

    #adds wins to player's money
    def win(self, bet):
        self.money = self.money + bet
    
    #subtracts losses to player's money
    def lose(self, bet):
        self.money = self.money - bet

    #gives player double their bet if they get blackjack
    def blackjack(self, bet):
        self.money = self.money + 2*bet

# game function
def run_game():
    p1 = player()           #player one
    amount1 = input("Enter your buy in amount: ")
    money = int(amount1)
    p1.buy_in(money)

    h1 = hand("player")
    h2 = hand("dealer")                                     

    amount2 = input("How much would you like to bet? ")
    bet = int(amount2)      #sets player's bet 

    for x in range(2):          #creates player's hand
        card1 = card()
        card1.set_values()
        h1.add_card(card1)

    print("Your cards:")
    h1.print_hand()
    print("Total = %d" % h1.total)

    print("Dealer:")
    for x in range(2):           #creates dealer's hand
       card2 = card()
       card2.set_values()
       h2.add_card(card2) 
       if (x ==0):
           card2.print_card()            
    
    move = "hit"                #assumption unless changed by user
    while (move == "hit"):
        move = input("Would you like to hit or stay? ")
        if (move == "stay"):
            print("Your total is %d" % h1.total)
            break
        new_card = card()
        new_card.set_values()
        h1.add_card(new_card)
        new_card.print_card()
        print("Total = %d" % h1.total)
        if (h1.total > 21):
            print("You bust!")
            p1.lose(bet)
            break

    print("Dealer:")
    h2.print_hand()
    

    


# main function
def main():
    run_game()

    
'''    card1 = card()          
    card1.set_values()
    card1.print_card()
    card2 = card()
    card2.set_values()
    card2.print_card()

    hand1 = hand()
    hand1.add_card(card1)
    hand1.add_card(card2)
    hand1.print_hand()

    print(hand1.total)  '''

main()

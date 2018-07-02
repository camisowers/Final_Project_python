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
        print("%d of %s" % (self.rank, self.suit))          #string formatting different than cout

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
    player_hand = []           #use list instead of vector
    total = 0                  #(int) total amount in hand 
    
    #adds a new card to the player's hand and keeps track of the total value
    def add_card(new_card):
        player_hand.append(new_card)
        total = total + new_card.rank
    
    #prints all the cards in the hand
    def print_hand(self):
        for x in player_hand:           #for loop that iterators through the list
            x.print_card()


# main function
def main():
    card1 = card()          
    card1.set_values()
    card2 = card()
    card2.set_values()

    hand1 = hand()
    hand1.add_card(card1)
    hand1.add_card(card2)
    hand1.print_hand()

main()

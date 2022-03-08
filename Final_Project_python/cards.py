import random          #random library

class card:
    suit = " "
    rank = 0
        
    #prints out rank and suit of card
    def print_card(self):                   
        print("%d of %s", (rank,suit))

    #overload < operator
 #   def __lt__(self,other):               
 #       return (self.rank < other.rank)
      
    def set_values(self):
        r1 = random.randrange(1,13)       #chooses random number correlating to type of card in deck
        set_rank = {                 #have to use a dictionary list instead of switch function
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
        rank = set_rank[r1]           #change the value of rank
        r2 = random.randrange(1,4)      #chooses a random number correlating to suit of card in deck
        set_suit = {
            1: "spades",
            2: "clubs",
            3: "hearts",
            4: "diamonds",
        } 
        suit = set_suit[r2]            #change the value of suit



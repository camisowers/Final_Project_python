class card:
    suit = " "
    rank = 0
        
    #prints out rank and suit of card
    def print_card(self):                   
        print("%d of %s")

    #overload < operator
    def __lt__(self,other):               
        return (self.rank < other.rank)

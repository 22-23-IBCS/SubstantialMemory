import random

class Card:

    def __init__(self, suit, name):
        self.suit = suit
        self.name = name

    def getName(self):
        return self.name

    def getSuit(self):
        return self.suit

    def getCard(self):
        return [self.suit, self.name]

class Deck:

    def __init__(self):
        self.cards = []
        suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
        for s in suits:
            for i in range(1, 14):
                if i == 1:
                    name = "Ace"
                elif i == 11:
                    name = "Jack"
                elif i == 12:
                    name = "Queen"
                elif i == 13:
                    name = "King"
                else:
                    name = str(i)

                C = Card(s, name)
                self.cards.append(C)

    def getCards(self):
        return self.cards

    def dealCard(self):
        newCard = random.choice(self.cards)
        self.cards.remove(newCard)
        return newCard

def calcHandValue(hand):
    total = 0
    for h in hand:
        name = h[1]
        if name == "Ace":
            total = total + 11
            if total > 21:
                total = total - 10
        elif name == "King" or name == "Queen" or name == "Jack" :
            total = total + 10
        else:
            total = total + int(name)
        
    return total
        

def main():

    print("Welcome to Blackjack!\n")
    i=1
    while i==1:
    D = Deck()
    userHand=[]
    userHand = [D.dealCard().getCard(), D.dealCard().getCard()]
    dealerHand=[]
    dealerHand = [D.dealCard().getCard(), D.dealCard().getCard()]

    print("Dealer hand:")
    print(dealerHand[1])
    print("")
    print(userHand)
    print("Your hand's value is :" + str(calcHandValue(userHand)))
    userHandvalue=calcHandValue(userHand)
    print("")
    bust=1 

    while True:
        if userHandvalue==21:
            print("BLACKJACK! YOU WIN!")
            bust=2
            break
        elif userHandvalue>21:
            print("YOU BUST\nDEALER WINS")
            bust=2
            break
        else:
            option = input("Type 1: Hit  or 2: Stand\n")
            if option == "1":
                userHand.append(D.dealCard().getCard())
                userHandvalue=calcHandValue(userHand)
            else:
                break
        print("")
        print(userHand)
        print("Your hand's value is :" + str(calcHandValue(userHand)))
        print("")

    while bust==1:
        print("")
        print("Dealer hand:")
        print(dealerHand)
        print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
        print("")
        dealerHandvalue =calcHandValue(dealerHand)
        print(dealerHand)
        if calcHandValue(dealerHand) < 17:
            print("Dealer hits!\n")
            dealerHand.append(D.dealCard().getCard())
            print("Dealer hand:")
            print(dealerHand)
            print("Dealer hand's value is :" + str(calcHandValue(dealerHand)))
            print("")
        else:
            print("Dealer stands!\n")
            if userHandvalue>dealerHandvalue:
                print("u win")
            else:
                print("dealer wins")
                bust=2
                
        if calcHandValue(dealerHand) > 21:
            print("Dealer bust!")
            print("u win")
            bust=2
        
        
        
        

if __name__ == "__main__":
    main()

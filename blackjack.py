# ver 1.9 Vlad Mott and Jon Eldridge and Jeff Mott
import random
import time

# Blackjack rules: https://bicyclecards.com/how-to-play/blackjack/
# Vegas Dealer's Handbook for Blackjack: https://www.vegas-aces.com/learn/deal-blackjack-07-the-game

############# Begin Class Definitions ###############
class Card():
    def __init__(self,suit,value,name):
        self.suit = suit
        self.value = value
        self.name = name
        self.lowAce = False

    def getValue(self):
        return self.value

    def isAce(self):
        return self.name == 'Ace'

    def printCard(self):
        print(self.name + " of " + self.suit)

    def setLowAce(self):
        if self.name == 'Ace':
            self.lowAce = True
    
    def isLowAce(self):
        return True if (self.lowAce==True) else False

class Deck():
    # Create a List to hold our Suits
    SUITS = ['Hearts','Diamonds','Clubs','Spades']
    # Create a List to hold our face cards
    #  (no jokers in this deck)
    FACE_CARDS = ['Jack','Queen','King','Ace']

    def __init__(self):
        # Create a Set to hold our cards
        self.cardsStillInDeck = set()
        
        ##### Create cards using for loops
        # first we'll create the numeric cards and add them to the deck
        for i in range(2,11):
            # create numeric cards in each of the four suits...
            for j in range(4):
                mySuit = self.SUITS[j]
                thisCard = Card(mySuit,i,str(i))
                self.cardsStillInDeck.add(thisCard)
        
        # now we need to create face cards and add them to the deck
        for k in range(4):
            myFaceCard = self.FACE_CARDS[k]
            # create face cards in each of the four suits...
            for j in range(4):
                mySuit = self.SUITS[j]
                myValue = 11 if (myFaceCard == 'Ace') else 10
                thisCard = Card(mySuit,myValue,myFaceCard)
                self.cardsStillInDeck.add(thisCard)

    def dealCard(self):
        # Pick a random card from the deck, remove it from deck
        #  we can't use the random function against a set, so we will cast the current set 
        #   of 'CardsStillInDeck' as a tuple.
        dealtCard = random.choice(tuple(self.cardsStillInDeck))
        # print(f'picked random card {DealtCard} from deck')
    
        # Remove the dealt card from the deck
        self.cardsStillInDeck.remove(dealtCard)
        print(f'Count of cards remaining in deck: {len(self.cardsStillInDeck)}')
        return dealtCard

    def printDeck(self):
        print('Count of cards in the deck:')
        print(len(self.cardsStillInDeck))
        for card in self.cardsStillInDeck:
            card.printCard()

class Hand():
    def __init__(self):
        self.cardsInHand = set()
        self.hiddenCard = None

    def addCard(self,card):
        self.cardsInHand.add(card)

    def takeCardsAway(self):
        self.cardsInHand.clear()

    def addHiddenCard(self,card):
        self.hiddenCard = card

    def checkForBlackjack(self):
        handValue = self.getHandValue() 
        if self.hiddenCard != None:
            handValue += self.hiddenCard.getValue()
        return handValue == 21

    def printHand(self):
        for card in self.cardsInHand:
            card.printCard()
        if self.hiddenCard != None:
            print("hidden card")
        #    self.hiddenCard.printCard()
        print(f"hand value = {self.getHandValue()}")

    def revealHiddenCard(self):
        print(f"Hidden Card is:")
        self.hiddenCard.printCard()
        self.cardsInHand.add(self.hiddenCard)
        self.hiddenCard = None

    def getHandValue(self):
        totalHandValue = 0
        for card in self.cardsInHand:
            totalHandValue += card.getValue()
        # switch from ace-high to ace-low if we are going to bust
        if totalHandValue > 21:
            for card in self.cardsInHand:
                if card.isAce() and not card.isLowAce():
                    card.setLowAce()
                    totalHandValue -= 10
        return totalHandValue

    def split(self):
        if not len(self.cardsInHand) == 2 or (len(self.cardsInHand) == 1 and self.hiddenCard != None):
            print("you cannot split this hand.") ##TBD split stuff later
    

class Player():
    def __init__(self,id):
        self.id = id

    HIT = "hit"
    STAND = "stand"
    QUIT = "quit"

    AVAIL_CHOICES = [HIT,STAND,QUIT]
    def play(self, hand):
        Choice = ""
        print(f"Player {self.id}, it is your turn.")
        print(f"Your hand is:")
        hand.printHand()
       
        while Choice.casefold() not in self.AVAIL_CHOICES:
            Choice = input('hit, stand, or quit: ')
        return Choice.casefold()


class PlayerAndHands():
    def __init__(self,player,hand):
        self.player = player
        self.hands = [hand]

    def splitHand(self,hand):
        hand.split() ## TBD split stuff

    def clearHands(self):
        self.hands.clear()

class Dealer():
    def __init__(self):
        self.players = []
        self.deck = None
        self.hand = None
    
    def addPlayer(self,id):
        hand = Hand()
        player = Player(id)
        playerAndHands = PlayerAndHands(player,hand)
        self.players.append(playerAndHands)

    def dealCards(self):
        ## deal first card to players
        for playerAndHands in self.players:
            for hand in playerAndHands.hands: ## this for loop will handy for splits (later)
                hand.addCard(self.deck.dealCard())

        ## deal first card to self
        self.hand.addCard(self.deck.dealCard())

        ## deal second card to players
        for playerAndHands in self.players:
            for hand in playerAndHands.hands: ## this for loop will handy for splits (later)
                hand.addCard(self.deck.dealCard())
                if hand.checkForBlackjack():
                    print("Blackjack!")


        ## deal second card to self
        self.hand.addHiddenCard(self.deck.dealCard())

    def startGame(self):
        self.deck = Deck()
        self.hand = Hand()
        self.dealCards()
        for playerAndHands in self.players:
            print(f"Player {playerAndHands.player.id} hand: ")
            for hand in playerAndHands.hands: 
                hand.printHand()
        print("Dealer hand: ")
        self.hand.printHand()

        ## check self for natural blackjack
        if self.hand.checkForBlackjack():
            print("Blackjack!")
            # check for bump against players on blackjack
            for playerAndHands in self.players:
                for hand in playerAndHands.hands:
                    if hand.checkForBlackjack():
                        print(f"BUMP! both player {playerAndHands.player.id} and the dealer have blackjack")
            quit()

    def getChoice(self):
        return Player.HIT ## TBD might be useful for splits and whatnot

   
    def playRound(self):
        for playerAndHands in self.players:
            for hand in playerAndHands.hands:
                while hand.getHandValue() < 21:
                    choice = playerAndHands.player.play(hand)
                    print(choice)

                    if choice == Player.HIT:
                        hand.addCard(self.deck.dealCard())
                        ## hand.printHand()
                        if hand.getHandValue() > 21:
                            ## busted
                            print("busted ya lout")
                    elif choice == Player.STAND:
                        print("player stands")
                        break
                    elif choice == Player.QUIT:
                        exit()
        #         ## Dealer reveals hidden card
       
        print('Dealer flips over their hidden card...')
        self.hand.revealHiddenCard()
        print("Dealer's hand is:")
        self.hand.printHand()

        while self.hand.getHandValue() < 17:
            choice = self.getChoice()
            if choice == Player.HIT:
                print("Dealer Hits.")
                self.hand.addCard(self.deck.dealCard())
                print("Dealer's hand is:")
                self.hand.printHand()


        if hand.getHandValue() > 21:
            print('Dealer BUSTS!  you win!')
            exit() 
        else:
            print('Dealer STANDS')
            time.sleep(2)

############# End Class Definitions ###########

dealer = Dealer()
playerCount = int(input('how many players? '))

for i in range(playerCount):
    dealer.addPlayer(i + 1)

dealer.startGame()

dealer.playRound()

quit()

Debug = False
PlayerHasNatural = False

# def FindTheWinner(DealerHandValue,PlayerHandValue):
#     ## compare hands to see who won
#     if DealerHandValue > PlayerHandValue:
#         print(f'Dealers {DealerHandValue} beats your {PlayerHandValue} ')
#         print('Dealer Wins!  game over.')
#         exit()
#     elif DealerHandValue < PlayerHandValue:
#         print(f'your {PlayerHandValue} beats Dealers {DealerHandValue} ')
#         print('You win! Congratulations!')
#         exit()
#     elif DealerHandValue == PlayerHandValue:
#         print(f'your {PlayerHandValue} matches Dealers {DealerHandValue} ')
#         print('Bump!  try another round.')
#         exit()


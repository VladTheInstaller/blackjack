# ver 1.7 Vlad Mott and Jon Eldridge and Jeff Mott
import random
import time

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
            # now we need to generate suits.  I'll grab them out of the Suits list
            for j in range(4):
                mySuit = self.SUITS[j]

                thisCard = Card(mySuit,i,str(i))
                self.cardsStillInDeck.add(thisCard)
        

        # now we need to create face cards and add them to the deck
        for k in range(4):
            myFaceCard = self.FACE_CARDS[k]
            # now we need to generate suits.  I'll grab them out of the Suits list
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
            print("hidden card value: ")
            self.hiddenCard.printCard()

    def revealHiddenCard(self):
        self.cardsInHand.add(self.hiddenCard)
        self.hiddenCard = None

    def getHandValue(self):
        totalHandValue = 0
        for card in self.cardsInHand:
            totalHandValue += card.getValue()
        # switch from ace-high to ace-low if we are going to bust
        while totalHandValue > 21:
            for card in self.cardsInHand:
                if card.isAce() and not card.isLowAce():
                    card.setLowAce()
                    totalHandValue -= 10
        return totalHandValue

    def split(self):
        if not len(self.cardsInHand) == 2 or (len(self.cardsInHand) == 1 and self.hiddenCard != None):
            print("you cannot split this hand.") ##TBD split stuff later
    

class Player():
    AVAIL_CHOICES = ['hit','stand','quit']
    def play(self, hand):
        Choice = ""
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
    
    def addPlayer(self):
        hand = Hand()
        player = Player()
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
        for index, playerAndHands in enumerate(self.players):
            print(f"Player {index + 1} hand: ")
            for hand in playerAndHands.hands: 
                hand.printHand()
        print("Dealer hand: ")
        self.hand.printHand()

        ## check self for natural blackjack
        if self.hand.checkForBlackjack():
            print("Blackjack!")
            # check for bump against players on blackjack
            for index, playerAndHands in enumerate(self.players):
                for hand in playerAndHands.hands:
                    if hand.checkForBlackjack():
                        print(f"BUMP! both player {index +1} and the dealer have blackjack")
            quit()




############# End Class Definitions ###########

dealer = Dealer()
playerCount = int(input('how many players? '))

for i in range(playerCount):
    dealer.addPlayer()

dealer.startGame()
## dealer.deck.printDeck()

quit()

Debug = False
PlayerHasNatural = False

# Blackjack rules: https://bicyclecards.com/how-to-play/blackjack/
# Vegas Dealer's Handbook for Blackjack: https://www.vegas-aces.com/learn/deal-blackjack-07-the-game

############ Lists vs Sets vs Tuples in Python ##########
#  	* A list can contain non-unique elements.  It uses square brackets []
#   * All elements in a Set must be unique.  It uses curly brackets {}
#         * A Python Set is an unordered collection of unique items. If we try to index into the set, 
#           we will get error "'set' object is not subscriptable."  The element is either in
#           the set or it isn't -- there is no index.
# 	* Tuples are immutable (read-only) lists.  you can't modify a tuple. They use parenthesis ()




 
# print('====================================')
# print(f'Count of cards in deck: {len(CardsStillInDeck)}')
# print('====================================')
# ################################################################


# ################################################################

# def player_choice():
#     AvailChoices = ['hit','stand','quit']
#     Choice = ""
#     while Choice.casefold() not in AvailChoices:
#         Choice = input('hit, stand, or quit: ')

#     return Choice.casefold()
# ################################################################

# def calculate_hand_value(hand): 


# #####################################################################
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

# ######################################################################
# # end functions
# ######################################################################        

# ######################################################################
# # Deal 2 cards to Player One
# ######################################################################
# if Debug == True:
#     # ask programmer to enter the players hand
#     PlayerOneHandFCString = input('player one first card: ')
#     PlayerOneHandSCString = input('player one second card: ')
#     PlayerOneHand.add(PlayerOneHandFCString.capitalize())
#     PlayerOneHand.add(PlayerOneHandSCString.capitalize())
#     # CardsStillInDeck.remove(PlayerOneHandFCString.capitalize())
#     # CardsStillInDeck.remove(PlayerOneHandSCString.capitalize())
    
    
#     # ask programmer to enter the dealers hand
#     DealerHandFUString = input ('dealer face-up card: ')
#     DealerHandFDString = input ('dealer face-down hole card:')
#     Hand.add(DealerHandFUString.capitalize())
#     Hand.add(DealerHandFDString.capitalize())
#     # CardsStillInDeck.remove(DealerHandFUString.capitalize())
#     # CardsStillInDeck.remove(DealerHandFDString.capitalize())
#     HiddenCard = DealerHandFDString

#     print('Player One hand at this time:')
#     print(PlayerOneHand)
#     print('--------------------------')
#     time.sleep(2)

#     print('Dealer hand at this time:')
#     print(Hand)
#     print('--------------------------')
#     time.sleep(2)
#     ############ end debug block ######################
# else:
#     for s in range(1,3):
#         # call the dealCard function
#         print('DEALING CARD TO PLAYER 1')
#         DealtCard = dealCard()

#         #print(f'adding {DealtCard} to players hand...')
#         PlayerOneHand.add(DealtCard)

#         print('Player One hand at this time:')
#         print(PlayerOneHand)
#         print('--------------------------')
#         time.sleep(2)

#     ######################################################################
#     # Deal 2 cards to Dealer
#     ######################################################################
#     for s in range(1,3):
#         # call the dealCard function
#         print('DEALING CARD TO THE DEALER')

#         if s == 1:
#             DealtCard = dealCard()
#             print(f'adding {DealtCard} to Dealers hand...')
#             Hand.add(DealtCard)
#             print('--------------------------')
#             time.sleep(2)
#         elif s==2:
#             HiddenCard = dealCard()
#             Hand.add(HiddenCard)
#             if Debug == True:
#                 print(f'DEBUG: hidden card is {HiddenCard}')
            
#             print(f'number of cards in dealers hand: {len(Hand)}')
#             print('--------------------------')
#             time.sleep(2)

#     print('Dealers hand at this time:')
#     for card in tuple(Hand):
#         if card == HiddenCard:
#             print('Hidden-Card')
#         else:
#             print(card)
#     print('--------------------------')

# ######################################################################
# # calculate hand values
# ######################################################################
# # get the Players hand value
# PlayerHandValue = calculate_hand_value(PlayerOneHand)
# #print(f'Player hand value: {PlayerHandValue}')

# # check to see if player got a natural blackjack
# if PlayerHandValue == 21:
#     print('You got BLACKJACK!!')
#     print('checking to see if Dealer also has natural blackjack...')
#     PlayerHasNatural = True
#     time.sleep(2)

# # get the dealers hand value
# # make a shallow copy of DealerHand so we can hide the face down hole card
# #DealerShownHand = DealerHand # this didn't work, because https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy
# DealerShownHand = Hand.copy() #note this is a shallow copy which is good enough for our needs
# DealerActualHandValue = calculate_hand_value(Hand)

# DealerShownHand.remove(HiddenCard)
# DealerShownHandValue = calculate_hand_value(DealerShownHand)
# print(f'Dealer hand value (shown cards only): {DealerShownHandValue}')
# time.sleep(2)

# if DealerShownHandValue == 10 or DealerShownHandValue == 11:
#     print(f'Dealers face-up card is worth 10 or 11 - checking for natural Blackjack...')
#     time.sleep(2)

#     # check to see if Dealer got a natural blackjack
#     if DealerActualHandValue == 21:
#         print(f'Dealer Hand: {Hand}')
#         print('Dealer has a natural Blackjack!')
    
#         time.sleep(2)
#         if PlayerHasNatural == True:
#             print('BUMP! you both have Natural blackjack.  Try again.')
#             exit()
#         else:
#             print('Dealer wins, because player does not have natural blackjack')
#             exit()
#     elif PlayerHasNatural == True:
#         print(f'Dealer Hand: {Hand}')
#         print('You win! Congrats!')
#         exit()    
#     else:
#         print('Dealer does not have a natural blackjack.  Play can continue...')
#         time.sleep(2)

# if PlayerHasNatural == True:
#     print('Dealer does not have natural blackjack.')
#     print('You win! Congrats!')
#     exit()  

# #####################################################################################
# # Continue prompting player for 'hit' or 'stand' until they stay or bust
# while PlayerHandValue <= 21:
#     ######################################################################
#     # Prompt player for choice
#     ######################################################################
#     print(f'Player hand value: {PlayerHandValue}')
#     print('--------------------------')

#     # call the player_choice function
#     Choice = player_choice()
#     #print(f'action chosen: {Choice}')

#     if Choice == 'hit':
#         ########### Player chose to Hit ###############
#         # call the dealCard function
#         DealtCard = dealCard()

#         print(f'adding {DealtCard} to players hand...')
#         PlayerOneHand.add(DealtCard)

#         print('Player One hand at this time:')
#         print(PlayerOneHand)
#         print('--------------------------')

#         # call the calculate_hand_value function
#         PlayerHandValue = calculate_hand_value(PlayerOneHand)
#         print(f'Player hand value: {PlayerHandValue}')
#         print(f'Dealer hand value: {DealerShownHandValue}')
        
#         if PlayerHandValue == 21:
#             print('Your hand is now worth 21. Please Stand.')

#         Choice = None

#     elif Choice == 'stand':
#         ########### Player chose to Stand ###############
#         #print('Player stands.')
        
#         ##################### Dealer's Turn ########################
#         # Dealer keeps hitting until they stay or bust
        
#         ## Dealer reveals hidden card
#         print('Dealer flips over their hidden card...')
#         time.sleep(2)

#         print(f'Dealers hidden card is: {HiddenCard}')
#         time.sleep(2)
#         print(f'Dealer Hand: {Hand}')
#         time.sleep(2)

#         # call the calculate_hand_value function
#         DealerActualHandValue = calculate_hand_value(Hand)
#         #print(f'Player hand value: {PlayerHandValue}')
#         print(f'Dealer hand value: {DealerActualHandValue}')  
#         time.sleep(2)      
        
#         while DealerActualHandValue < 17:
#             # calculate if dealer hits or stands
#                 print('Dealer chooses to Hit')
                
#                 # sleep for a few seconds
#                 time.sleep(2)

#                 # call the dealCard function
#                 DealtCard = dealCard()

#                 print(f'adding {DealtCard} to dealers hand...')
#                 Hand.add(DealtCard)
#                 time.sleep(2)
#                 print('----------------------------')
#                 #print(f'number of cards in dealers hand: {len(DealerHand)}')

#                 print('Dealers hand at this time:')
#                 print(Hand)
#                 print('--------------------------') 

#                 # call the calculate_hand_value function
#                 DealerActualHandValue = calculate_hand_value(Hand)
#                 print(f'Player hand value: {PlayerHandValue}')
#                 print(f'Dealer hand value: {DealerActualHandValue}')
#                 Choice = None
#                 time.sleep(2)

#         if DealerActualHandValue > 21:
#             print('Dealer BUSTS!  you win!')
#             exit() 
#         else:
#             print('Dealer STANDS')
#             time.sleep(2)

#             ###### everyone stands, time to calculate the winner        
#             ## Find the Winner
#             WinnerName = FindTheWinner(DealerActualHandValue,PlayerHandValue)

#     elif Choice == 'quit':
#         print('quitting game.')
#         exit()

# # player busts
# if PlayerHandValue > 21:
#     print(f'your {PlayerHandValue} is a BUST! better luck next time.')



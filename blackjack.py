# ver 1.1 Vlad Mott and Jon Eldridge
import random
import time

PlayerHasNatural = False

# Blackjack rules: https://bicyclecards.com/how-to-play/blackjack/

############ Lists vs Sets vs Tuples in Python ##########
#  	* A list can contain non-unique elements
#   * All elements in a Set must be unique.
#         * A Python Set is an unordered collection of unique items. If we try to index into the set, 
#           we will get error "'set' object is not subscriptable."  The element is either in
#           the set or it isn't -- there is no index.
# 	* Tuples are immutable (read-only) lists.  you can't modify a tuple. 

# Create a Set to hold our cards
CardsStillInDeck = set()
# Create a Set to hold the players hand
PlayerOneHand = set()
# Create a Set to hold the Dealers hand
DealerHand = set()
# Create a List to hold our Suits
Suits = ['Hearts','Diamonds','Clubs','Spades']
# Create a List to hold our face cards
#  (no jokers in this deck)
FaceCards = ['Jack','Queen','King','Ace']

##### Create cards using for loops
# first we'll create the numeric cards and add them to the deck
for i in range(2,11):
    # now we need to generate suits.  I'll grab them out of the Suits list
    for j in range(4):
        MySuit = Suits[j]
        # print(f'adding {i} of {MySuit} to deck...')
        ThisCard = str(i) + '-' + MySuit
        CardsStillInDeck.add(ThisCard)
    
# now we need to create face cards and add them to the deck
for k in range(4):
    MyFaceCard = FaceCards[k]
    # now we need to generate suits.  I'll grab them out of the Suits list
    for j in range(4):
        MySuit = Suits[j]
        # print(f'adding {MyFaceCard} of {MySuit} to deck...')
        ThisCard = str(MyFaceCard) + '-' + MySuit
        CardsStillInDeck.add(ThisCard)
 
print('====================================')
print(f'Count of cards in deck: {len(CardsStillInDeck)}')
print('====================================')
################################################################

def deal_card():
    # Pick a random card from the deck, remove it from deck
    #  we can't use the random function against a set, so we will cast the current set 
    #   of 'CardsStillInDeck' as a tuple.
    DealtCard = random.choice(tuple(CardsStillInDeck))
    # print(f'picked random card {DealtCard} from deck')
   
    # Remove the dealt card from the deck
    CardsStillInDeck.remove(DealtCard)
    print(f'Count of cards remaining in deck: {len(CardsStillInDeck)}')
    return DealtCard
################################################################

def player_choice():
    AvailChoices = ['hit','stand','quit']
    Choice = ""
    while Choice.casefold() not in AvailChoices:
        Choice = input('hit, stand, or quit: ')

    return Choice.casefold()
################################################################

def calculate_hand_value(hand): 
    TotalHandValue = 0
    HandValueList = []
    for card in hand:
        #print(f'card is: {card}')
        CardValue = card.split('-')
        
        if CardValue[0] == 'Ace':
            IntCardValue = int(11)
        elif CardValue[0] in FaceCards:
            IntCardValue = int(10)
        else:
            IntCardValue = int(CardValue[0])
        
        #print(f'card value is: {IntCardValue}')
        #print('adding card value to array')
        HandValueList.append(IntCardValue)
    
    TotalHandValue = sum(HandValueList)
    return TotalHandValue

#####################################################################
def FindTheWinner(DealerHandValue,PlayerHandValue):
    ## compare hands to see who won
    if DealerHandValue > PlayerHandValue:
        print(f'Dealers {DealerHandValue} beats your {PlayerHandValue} ')
        print('Dealer Wins!  game over.')
        exit()
    elif DealerHandValue < PlayerHandValue:
        print(f'your {PlayerHandValue} beats Dealers {DealerHandValue} ')
        print('You win! Congratulations!')
        exit()
    elif DealerHandValue == PlayerHandValue:
        print(f'your {PlayerHandValue} matches Dealers {DealerHandValue} ')
        print('Bump!  try another round.')
        exit()

######################################################################
# Deal 2 cards to Player One
######################################################################
for s in range(1,3):
    # call the deal_card function
    print('DEALING CARD TO PLAYER 1')
    DealtCard = deal_card()

    #print(f'adding {DealtCard} to players hand...')
    PlayerOneHand.add(DealtCard)

    print('Player One hand at this time:')
    print(PlayerOneHand)
    print('--------------------------')
    time.sleep(2)

######################################################################
# Deal 2 cards to Dealer
######################################################################
for s in range(1,3):
    # call the deal_card function
    print('DEALING CARD TO THE DEALER')

    if s == 1:
        DealtCard = deal_card()
        print(f'adding {DealtCard} to Dealers hand...')
        DealerHand.add(DealtCard)
        print('--------------------------')
        time.sleep(2)
    elif s==2:
        HiddenCard = deal_card()
        DealerHand.add(HiddenCard)
        print(f'DEBUG: hidden card is {HiddenCard}')
        print(f'number of cards in dealers hand: {len(DealerHand)}')
        print('--------------------------')
        time.sleep(2)

print('Dealers hand at this time:')
for card in tuple(DealerHand):
    if card == HiddenCard:
        print('Hidden-Card')
    else:
        print(card)
print('--------------------------')

######################################################################
# calculate hand values
######################################################################
# get the Players hand value
PlayerHandValue = calculate_hand_value(PlayerOneHand)
#print(f'Player hand value: {PlayerHandValue}')

# check to see if player got a natural blackjack
if PlayerHandValue == 21:
    print('You got BLACKJACK!!')
    print('checking to see if Dealer also has natural blackjack...')
    PlayerHasNatural = True
    time.sleep(2)

#DealerShownHand = DealerHand # this didn't work, because https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy
DealerShownHand = DealerHand.copy() #note this is a shallow copy which is good enough for our needs
DealerShownHand.remove(HiddenCard)

DealerActualHandValue = calculate_hand_value(DealerHand)
DealerShownHandValue = calculate_hand_value(DealerShownHand)

print(f'Dealer hand value (shown cards only): {DealerShownHandValue}')
time.sleep(2)

if DealerShownHandValue == 10 or DealerShownHandValue == 11:
    print(f'Dealers face-up card is worth 10 or 11 - checking for natural Blackjack...')
    time.sleep(2)

    # check to see if Dealer got a natural blackjack
    if DealerActualHandValue == 21:
        print(f'Dealer Hand: {DealerHand}')
        print('Dealer has a natural Blackjack!')
    
        time.sleep(2)
        if PlayerHasNatural == True:
            print('BUMP! you both have Natural blackjack.  Try again.')
            exit()
        else:
            print('Dealer wins, because player does not have natural blackjack')
            exit()
    elif PlayerHasNatural == True:
        print(f'Dealer Hand: {DealerHand}')
        print('You win! Congrats!')
        exit()    
    else:
        print('Dealer does not have a natural blackjack.  Play can continue...')
        time.sleep(2)

if PlayerHasNatural == True:
    print('Dealer does not have natural blackjack.')
    print('You win! Congrats!')
    exit()  

#####################################################################################
# Continue prompting player for 'hit' or 'stand' until they stay or bust
while PlayerHandValue < 22:
    ######################################################################
    # Prompt player for choice
    ######################################################################
    print(f'Player hand value: {PlayerHandValue}')
    print('--------------------------')

    # call the player_choice function
    Choice = player_choice()
    #print(f'action chosen: {Choice}')

    if Choice == 'hit':
        ########### Player chose to Hit ###############
        # call the deal_card function
        DealtCard = deal_card()

        print(f'adding {DealtCard} to players hand...')
        PlayerOneHand.add(DealtCard)

        print('Player One hand at this time:')
        print(PlayerOneHand)
        print('--------------------------')

        # call the calculate_hand_value function
        PlayerHandValue = calculate_hand_value(PlayerOneHand)
        print(f'Player hand value: {PlayerHandValue}')
        print(f'Dealer hand value: {DealerShownHandValue}')
        Choice = None

    elif Choice == 'stand':
        ########### Player chose to Stand ###############
        #print('Player stands.')
        
        ##################### Dealer's Turn ########################
        # Dealer keeps hitting until they stay or bust
        
        ## Dealer reveals hidden card
        print('Dealer flips over their hidden card...')
        time.sleep(2)

        print(f'Dealers hidden card is: {HiddenCard}')
        time.sleep(2)
        print(f'Dealer Hand: {DealerHand}')
        time.sleep(2)

        # call the calculate_hand_value function
        DealerActualHandValue = calculate_hand_value(DealerHand)
        #print(f'Player hand value: {PlayerHandValue}')
        print(f'Dealer hand value: {DealerActualHandValue}')  
        time.sleep(2)      
        
        while DealerActualHandValue < 17:
            # calculate if dealer hits or stands
                print('Dealer chooses to Hit')
                
                # sleep for a few seconds
                time.sleep(2)

                # call the deal_card function
                DealtCard = deal_card()

                print(f'adding {DealtCard} to dealers hand...')
                DealerHand.add(DealtCard)
                time.sleep(2)
                print('----------------------------')
                #print(f'number of cards in dealers hand: {len(DealerHand)}')

                print('Dealers hand at this time:')
                print(DealerHand)
                print('--------------------------') 

                # call the calculate_hand_value function
                DealerActualHandValue = calculate_hand_value(DealerHand)
                print(f'Player hand value: {PlayerHandValue}')
                print(f'Dealer hand value: {DealerActualHandValue}')
                Choice = None
                time.sleep(2)

        if DealerActualHandValue > 21:
            print('Dealer BUSTS!  you win!')
            exit() 
        else:
            print('Dealer STANDS')
            time.sleep(2)

            ###### everyone stands, time to calculate the winner        
            ## Find the Winner
            WinnerName = FindTheWinner(DealerActualHandValue,PlayerHandValue)

    elif Choice == 'quit':
        print('quitting game.')
        exit()
            
if PlayerHandValue > 21:
    print(f'your {PlayerHandValue} is a BUST! better luck next time.')



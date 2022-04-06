# ver 0.7 Vlad Mott
#Import the Random module
import random

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
    #  we can't use the random function against a set, so we will cast the current set of 'CardsStillInDeck' as a tuple.
    DealtCard = random.choice(tuple(CardsStillInDeck))

    print(f'picked random card {DealtCard} from deck')
    #print(f'removing {DealtCard} from deck')
    CardsStillInDeck.remove(DealtCard)
    #print(f'Count of cards remaining in deck: {len(CardsStillInDeck)}')
    
    return DealtCard
################################################################

def player_choice():
    AvailChoices = ['hit','stand']
    Choice = ""
    while Choice.casefold() not in AvailChoices:
        Choice = input('hit or stand: ')

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

######################################################################
# Deal 2 cards to Player One
######################################################################
for s in range(1,3):
    # call the deal_card function
    DealtCard = deal_card()

    #print(f'adding {DealtCard} to players hand...')
    PlayerOneHand.add(DealtCard)

    print('Player One hand at this time:')
    print(PlayerOneHand)
    print('--------------------------')

######################################################################
# Deal 2 cards to Dealer
######################################################################
for s in range(1,3):
    # call the deal_card function
    DealtCard = deal_card()

    #print(f'adding {DealtCard} to Dealers hand...')
    DealerHand.add(DealtCard)

    print('Dealers hand at this time:')
    print(DealerHand)
    print('--------------------------')

######################################################################
# calculate hand values
######################################################################
# get the Players hand value
PlayerHandValue = calculate_hand_value(PlayerOneHand)
print(f'Player hand value: {PlayerHandValue}')

DealerHandValue = calculate_hand_value(DealerHand)
print(f'Dealer hand value: {DealerHandValue}')
print('--------------------------')

######################################################################
# Prompt player for choice
######################################################################
# call the player_choice function
Choice = player_choice()
print(f'action chosen: {Choice}')

if Choice == 'hit':
    ########### Player chose to Hit ###############
    # call the deal_card function
    DealtCard = deal_card()

    #print(f'adding {DealtCard} to players hand...')
    PlayerOneHand.add(DealtCard)

    print('Player One hand at this time:')
    print(PlayerOneHand)
    print('--------------------------')

    # call the calculate_hand_value function
    HandValue = calculate_hand_value(PlayerOneHand)
    print(f'Player hand value: {HandValue}')

elif Choice == 'stand':
    ########### Player chose to Stand ###############
    print('Player stands.')
 
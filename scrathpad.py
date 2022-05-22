# Create a Set to hold our cards
from email.headerregistry import HeaderRegistry
from zipfile import _SupportsReadSeekTell


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
    for j in range(0,4):
        MySuit = Suits[j]
        #print(f'adding {i} of {MySuit} to deck...')
        ThisCard = str(i) + '-' + MySuit
        print(f'adding {ThisCard} to deck')
        CardsStillInDeck.add(ThisCard)

# now we need to create face cards and add them to the deck
for k in range(4):
    MyFaceCard = FaceCards[k]
    # now we need to generate suits.  I'll grab them out of the Suits list
    for j in range(4):
        MySuit = Suits[j]
        ThisCard = str(MyFaceCard) + '-' + MySuit
        print(f'adding {ThisCard} to deck')
        CardsStillInDeck.add(ThisCard)

# DealerShownHand

10-Hearts,jack-Spades,3-clubs

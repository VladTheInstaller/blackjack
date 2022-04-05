# ver 0.2 Vlad Mott
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
# first we'll create the numberic cards and add them to the deck
for i in range(2,11):
    # now we need to generate suits.  I'll grab them out of the Suits list
    for j in range(4):
      
      
      MySuit = Suits[j]

      print(f'adding {i} of {MySuit} to deck...')
      ThisCard = str(i) + '-' + MySuit
      #print(f'dude, this card is {ThisCard}')
      CardsStillInDeck.add(ThisCard)


# now we need to create face cards and add them to the deck
for k in range(4):
  MyFaceCard = FaceCards[k]

  # now we need to generate suits.  I'll grabe them out of the Suits list
  for j in range(4):
    MySuit = Suits[j]

    print(f'adding {MyFaceCard} of {MySuit} to deck...')
    ThisCard = str(MyFaceCard) + '-' + MySuit
    #print(f'dude, this card is {ThisCard}')
    CardsStillInDeck.add(ThisCard)
 
print('====================================')

print(f'Count of cards in deck: {len(CardsStillInDeck)}')
print('====================================')

def deal_card():
  # Pick a random card from the deck, remove it from deck, add to hand
  #  we can't use the random function against a set, so we will cast the current set of 'CardsStillInDeck' as a tuple.
  DealtCard = random.choice(tuple(CardsStillInDeck))

  print(f'picked random card {DealtCard} from deck')
  return DealtCard

######################################################################
# Deal 2 cards to Player One
######################################################################
for s in range(1,3):
  # call the deal_card function
  DealtCard = deal_card()

  print(f'removing {DealtCard} from deck')
  CardsStillInDeck.remove(DealtCard)

  print(f'adding {DealtCard} to players hand...')
  PlayerOneHand.add(DealtCard)

  print('Player One hand at this time:')
  print(PlayerOneHand)

  print(f'Count of cards in deck: {len(CardsStillInDeck)}')
  print('--------------------------')

######################################################################
# Deal 2 cards to Dealer
######################################################################
for s in range(1,3):
  # call the deal_card function
  DealtCard = deal_card()

  print(f'removing {DealtCard} from deck')
  CardsStillInDeck.remove(DealtCard)

  print(f'adding {DealtCard} to Dealers hand...')
  DealerHand.add(DealtCard)

  print('Dealers hand at this time:')
  print(DealerHand)

  print(f'Count of cards in deck: {len(CardsStillInDeck)}')
  print('--------------------------')


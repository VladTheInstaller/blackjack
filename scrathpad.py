FaceCards = ['Jack','Queen','King','Ace']
PlayerOneHand = {'Ace-Clubs', '7-Hearts'}

TotalHandValue = 0
HandValueList = []
for card in PlayerOneHand:
    print(f'card is: {card}')
    CardValue = card.split('-')
    
    if CardValue[0] == 'Ace':
        IntCardValue = int(11)
    elif CardValue[0] in FaceCards:
        IntCardValue = int(10)
    else:
        IntCardValue = int(CardValue[0])
    
    print(f'card value is: {IntCardValue}')
    print('adding card value to array')
    HandValueList.append(IntCardValue)

TotalHandValue = sum(HandValueList)
print(TotalHandValue)




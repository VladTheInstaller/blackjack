# Create an ArrayList to hold our cards
[System.Collections.ArrayList]$CardStillInDeck = @()

# Create an ArrayList to hold the players hand
[System.Collections.ArrayList]$PlayerOneHand = @()

# create an array to hold our Suits
$Suits = @('Hearts','Diamonds','Clubs','Spades')

# create an array to hold our face card values
#  (no jokers in this deck)
$FaceCards = @('Jack','Queen','King','Ace')


##### Create cards using for loops
# first we'll create the numeric cards and add them to the deck
for ($i=2; $i -le 10; $i++)
{
    # now we need to generate suits. I'll grab them out of the $Suits array
    For ($j=0; $j -le 3; $j++)
    {
        $MySuit = $Suits[$j]
        
        #Write-Host "adding $i of $MySuit to deck..."
        [string]$ThisCard = [string]$i + "-" + $MySuit
        $CardStillInDeck += $ThisCard
    }
}

# now we need to create face cards and add them to the deck
for ($k = 0; $k -le 3; $k++)
{
    $MyFaceCard = $FaceCards[$k]

    # now we need to generate suits. I'll grab them out of the $Suits array
    For ($j=0; $j -le 3; $j++)
    {
        $MySuit = $Suits[$j]

        #Write-Host "adding $MyFaceCard of $MySuit to deck..."
        [string]$ThisCard = [string]$MyFaceCard + "-" + $MySuit
        $CardStillInDeck += $ThisCard
    }
}

Write-Host "=====================================" -f cyan
$CardStillInDeck
Write-Host "Count of cards in deck: " $CardStillInDeck.Count
Write-Host "=====================================" -f cyan

######################################################################
# Deal 5 cards to Player One
######################################################################
for ($s=1; $s -le 5; $s++)
{
    # Pick a random card from the deck, remove it from deck, add to hand
    $DealtCard = Get-Random -InputObject $CardStillInDeck

    Write-Host "picked random card $DealtCard from deck" -f green

    Write-Host "removing $DealtCard from deck..."
    $CardStillInDeck.Remove($DealtCard)

    Write-Host "adding $DealtCard to player's hand..."
    $PlayerOneHand += $DealtCard

    Write-Host "Player One hand at this time: "
    $PlayerOneHand

    Write-Host "Count of cards in deck: " $CardStillInDeck.Count
    Write-Host "----------------------"
}

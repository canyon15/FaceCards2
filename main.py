"""
card class:
lays out card data type with value (1-13 or Ace - King) and suit (heart, spade, club, diamond)
"""
# Datetime is used to get random numbers.
from datetime import datetime

# Card class card has a value and a suit.
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    # sets card value, between 1 and 13.
    def setValue(self, value):
        if (value >= 1 and value <= 13):
            self.value = value
        else:
            print("error: card value must be between 1 and 13, check card class.")
    # returns value and translates face cards.
    def getValue(self):
        if (self.value == 1):
            self.value = "Ace"
        if (self.value == 11):
            self.value = "Jack"
        if (self.value == 12):
            self.value = "Queen"
        if (self.value == 13):
            self.value = "King"
        return self.value
    # Sets and enforces suits
    def setSuit(self, suit):
        if (suit == "heart" or "spade" or "club" or "diamond"):
            self.suit = suit
        else:
            print("error: card suit must be 1 of 4 strings, check card class.")
    # returns suit
    def getSuit(self):
        return self.suit
    # Puts cards in a printable string
    def __str__(self):
        v = self.getValue()
        s = self.getSuit()
        text = "{} of {}'s ".format(v, s)
        return text

# Fills deck with standard 52 cards of each 
# value and suit
def newDeck():
    s = 0
    deck = []
    while (s <= 3):
       v = 1
       if (s == 0):
           suit = "heart"
       elif (s == 1):
           suit = "spade"
       elif (s == 2):
           suit = "club" 
       elif (s == 3):
           suit = "diamond"
       while (v <= 13):
           deck.append(Card(v, suit))
           v += 1
       s += 1
    return deck

# Display's cards from a given list.
def showDeck(deck):
    for x in range(len(deck)):
        print(deck[x])

# Gets "random" numbers from the time for 
# shuffling purposes.
def randomNum():
    nums = []
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time)
# This part turn the string timestamp into
# 6 different integers
    nums.append(int(time[0]) + 1)
    nums.append(int(time[1]) + 1)
    nums.append(int(time[3]) + 1)
    nums.append(int(time[4]) + 1)
    nums.append(int(time[6]) + 1)
    nums.append(int(time[7]) + 1)  
    return nums

# It mixes the cards about.
def blend(deck):
    nums = randomNum()
    newDeck = []
    i = 0
    while (len(deck) > 11):
        if (i >= 5):
            i = 0
        newDeck.append(deck[nums[i]])
        del deck[nums[i]]
        i += 1
        n = len(deck) - nums[i]
        newDeck.append(deck[n])
        del deck[n]
        i += 1
# It changes here so as to avoid drawing cards
# that aren't there
    while (len(deck) > 0):
        if (i >= 5):
            i = 0
        card = deck[0]
        newDeck.insert(nums[i], card)
        del deck[0]
        i += 1
    return newDeck

# It takes the top half(ish) (7-33)
# and put it on the bottom
def cut(deck):
    n = randomNum()
    num = 0
    #get the sum of list of random numbers
    for x in range(len(n)):
        num = num + n[x]

    while (num > 0):
        card = deck.pop()
        deck.append(card)
        num -= 1
    return deck

# Shuffles the cards
def shuffle(deck):
    deck = blend(deck)
    deck = cut(deck)
    # Because once is never enough
    deck = blend(deck)
    return deck

# Take a card from hand or deck
def drawCard(deck):
    card = deck.pop()
    return card

# display's user menu prompt.
def showPrompt():
    print("(1) Draw Card")
    print("(2) Discard")
    print("(3) Shuffle Deck")
    print("(4) Show Hand")
    print("(5) Show Prompt")
    # (6) Show Deck
    print("(0) Quit")

# Takes functions and makes 
# them into something usable.
def main():
    # Variables
    hand = []
    deck = []
    discard = []
    deck = newDeck()
    choice = 5
    # Main menu loop
    while (choice != 0):
        if not deck:
            deck = discard
            discard.clear()
            shuffle(deck)
        choice = int(input(">"))
        if (choice == 1):
            card = drawCard(deck)
            hand.append(card)
        elif (choice == 2):
            card = drawCard(hand)
            discard.append(card)
        elif (choice == 3):
            deck = shuffle(deck)
        elif (choice == 4):
            print ("Cards in your hand: ")
            showDeck(hand)
        elif (choice == 5):
            showPrompt()
        elif (choice == 6):
            showDeck(deck)
        else:
            print ("Invalid input!")


   


if __name__ == "__main__":
    main()
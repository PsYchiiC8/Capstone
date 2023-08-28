"""This file is primarily to hold the basic functions of a card game- making a deck, shuffling, and distribution(for starting)"""

import random

def make_deck():
    colors = ["R", "B", "G", "Y"]           #the 4 colors- red, blue, green, yellow simplified to first letter
    specials = ["R", "S", "+2", "+4", "W"]
    deck = []                               #the deck list

    for color in colors:                    #cycles through the colors list
        for i in range(10):                 #generates the numbers
            for j in range(2):
                deck.append((color, str(i)))      #adds the card to the list with set values

    for card in specials:
        for color in colors:
            for i in range(2):
                if card != "+4" and card != "W":      #this if statement is to make sure the card is a card that can have
                    deck.append((color, card))                          #color since +4 and wild technically don't have a color
        if card == "+4" or card == "W":
            for num in range(4):
                deck.append((None, card))

    return deck

def shuffle(cards):                 #shuffle deck function
    for i in range(5000):           #pulls 1 random card out, putting it in the back of the deck and then removing it(from the original index), repeat x5000
        index = random.randint(0, len(cards) - 1)

        cards.append(cards[index])
        cards.pop(index)

    return cards

def distribute(cards):        #distributes the cards at the start of the game,7 cards each, take from  top(starting from index 0 of the 1st card)
    player_1 = []
    player_2 = []
    player_3 = []
    player_hands = [player_1, player_2, player_3]
    for j in range(7):
        player_1.append((cards.pop(0)))
        player_2.append((cards.pop(0)))
        player_3.append((cards.pop(0)))

    return player_hands, cards


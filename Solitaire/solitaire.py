from random import *

class Card:

    def __init__(self, suit, number):  # Initialization of suits

        self.revealed = False

        self.suit = suit

        if 1 <= number <= 13:  # Initialization of numbers
            self.number = number
        else:
            raise Exception("Invalid card number.")

    def __str__(self):

        numDict = {
            1: 'A',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: 'T',
            11: 'J',
            12: 'Q',
            13: 'K'
        }

        suitDict = {
            0: 'H',
            1: 'D',
            2: 'S',
            3: 'C'
        }

        return numDict[self.number] + suitDict[self.suit]

    def getColor(self):

        red = [0,1]
        black = [2,3]

        if self.suit in red:
            return 'Red'
        else:
            return 'Black'

    def isMovable(self, prevCard):
        if (self.getColor() != prevCard.getColor()) and (self.number == prevCard.number - 1):
            return True
        else:
            return False

class Deck:
    def __init__(self):
        self.deck = []
        self.upCount = 0

    def drawCard(self):
        self.upCount += 1
        self.deck[self.upCount].revealed = True

    def makeDeck(self):
        for s in range(4):
            for n in range(1,14):
                card = Card(s, n)
                self.deck.append(card)
        shuffle(self.deck)

    def placeCard(self):
        self.deck.pop(-self.upCount)

    def removeCard(self):
        return self.deck.pop()

class Tableau:
    def __init__(self, cardList):
        self.tableau = cardList
        cardList[-1].revealed = True

    def addCards(self, cardList):
        if cardList[0].isMovable(self.tableau[-1]):
            self.tableau += cardList
        else:
            raise Exception('Invalid card placement.')

    def removeCards(self, cardCount):
        cardList = self.tableau[-cardCount:]
        self.tableau = self.tableau[:-cardCount]
        self.tableau[-1].revealed = True
        return cardList

class Foundation:
    def __init__(self, suit):
        self.foundation = []
        self.suit = suit
        self.number = 0
    def addCard(self, card):
        if (card.suit == self.suit) and (card.number == self.number + 1):
            self.foundation.append(card)
        else:
            raise Exception('Invalid card placement.')
    def removeCard(self, card):
        return self.foundation.pop()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.makeDeck()
        self.tableauList = []
        for i in range(1,8):
            tableauCards = []
            for c in range(i):
                tableauCards.append(self.deck.removeCard())
            self.tableauList.append(Tableau(tableauCards))
        self.foundationList = []
        for i in range(4):
            self.foundationList.append(Foundation(i))
        self.hand = []
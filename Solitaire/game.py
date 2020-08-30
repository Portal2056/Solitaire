import pygame
import solitaire
import random

game = solitaire.Game()

cardDict = {}

for suit in range(0,4): # String-to-image for loop
    for number in range(1,14):
        currentCard = solitaire.Card(suit, number)
        cardDict[str(currentCard)] = pygame.image.load('Card Sprites\\' + str(currentCard) + '.png')

cardBack = pygame.image.load('Card Sprites\\CardBack.png')
tasbleauSpace = pygame.image.load('Card Sprites\\TableauSpace.png')
foundationSpace = pygame.image.load('Card Sprites\\FoundationSpace.png')

class Tableau:
    def __init__(self, tableau, x, y, horizAlign, vertAlign):
        self.image = pygame.image.load('Card Sprites\\TableauSpace.png')
        self.tableau = tableau
        self.x = x
        self.y = y
        self.horizAlign = horizAlign
        self.vertAlign = vertAlign

    def drawTo(self, screen):
        width = screen.get_width()
        height = screen.get_height()
        trueX = self.x
        trueY = self.y

        if self.horizAlign:
            trueX = width - trueX
        if self.vertAlign:
            trueY = height - trueY
        truePos = (trueX, trueY)

        if self.tableau.tableau == []:
            screen.blit(self.image, truePos)
        else:
            for card in self.tableau.tableau:
                pass
class Foundation:
    def __init__(self, foundation, x, y, horizAlign, vertAlign):
        self.image = pygame.image.load('Card Sprites\\FoundationSpace.png')
        self.foundation = foundation
        self.x = x
        self.y = y
        self.horizAlign = horizAlign
        self.vertAlign = vertAlign

# Define some colors
BACKGROUND = (0, 96, 0)
WHITE = (255, 255, 255)

pygame.init()

w = 1600
h = 900

# Set the width and height of the screen [width, height]
size = (w, h)

screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

pygame.display.set_caption("Solitaire")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND)
    # --- Drawing code should go here
    # Next card drawn from deck is offset 30pz
    screen.blit(cardBack, (50, 50))

    screen.blit(cardDict['TS'], (185, 50))
    screen.blit(cardDict['TS'], (215, 50))
    screen.blit(cardDict['TS'], (245, 50))

    screen.blit(cardDict['TS'], (405, 50))
    screen.blit(cardDict['TS'], (535, 50))
    screen.blit(cardDict['TS'], (665, 50))
    screen.blit(cardDict['TS'], (795, 50))
    screen.blit(cardDict['TS'], (925, 50))
    screen.blit(cardDict['TS'], (1055, 50))
    # screen.blit(cardDict['TS'], (1185, 50))

    screen.blit(cardBack, (50, 675))
    screen.blit(cardBack, (185, 675))
    screen.blit(cardBack, (50, 490))
    screen.blit(cardBack, (185, 490))

    for t in range(16):
        screen.blit(cardDict['TS'], (1185, 50 + t * 48))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

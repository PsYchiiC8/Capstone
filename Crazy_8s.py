"""
needs:
    make deck- RBGY, 0-10, 2 each(color & number so there are two R3, B9, Y6, etc), "Crazy Cards"/special cards
        (skip, +2, +4 & change color, wild, reverse)                                                                        done
    shuffling for beginning & when the pickup deck is empty                                                                 done
    player(s), 2 or more
    distribution of cards for +2/+4 and when the game starts-   in progress- mostly done
    taking card if there isn't the number or color needed-      works for human, not for ai(not really)
    choosing a card & removing it from the player's hand-       done
    discarded/used cards to shuffle later-                      should work, haven't tested that far
"""

import Crazy_8s_util as gf      # gf for game functions
from player_functions import*
import random
import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Crazy 8's")
screen.fill((0, 0, 175))

CARD_FONT = pygame.font.SysFont('courier', 20)
END_FONT = pygame.font.SysFont('courier', 40)

def update_screen(players, current_card, color):
    screen.fill((0, 0, 175))

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)                 #The colors

    the_color = BLACK
    if current_card[0] is None:
        if color == "R":
            the_color = RED
        elif color == "B":
            the_color = BLUE
        elif color == "G":
            the_color = GREEN
        elif color == "Y":
            the_color = YELLOW
    elif current_card[0] == "R":
        the_color = RED
    elif current_card[0] == "B":
        the_color = BLUE
    elif current_card[0] == "Y":
        the_color = YELLOW
    elif current_card[0] == "G":
        the_color = GREEN

    pygame.time.delay(500)

    pygame.draw.rect(screen, WHITE, (174, 200, 74, 100), 2)         #border of unused deck
    pygame.draw.rect(screen, BLACK, (176, 202, 71, 97))             #filling of unused deck

    pygame.draw.rect(screen, WHITE, (251, 200, 74, 100), 2)         #border of current card
    pygame.draw.rect(screen, the_color, (253, 202, 71, 97))         #filling of current card
    text = CARD_FONT.render(current_card[1], 1, WHITE)
    screen.blit(text, (288, 250))           #draws the unused deck and the current card

    # This block and the next are for the AI players
    corner_y = 213                                                      #AI hand(player two, AI #1)
    corner_y -= (35 * int(len(players[1].hand)/2))
    for i in range(len(players[1].hand)):
        pygame.draw.rect(screen, WHITE, (0, corner_y, 100, 74), 2)
        pygame.draw.rect(screen, BLACK, (2, corner_y + 2, 97, 70))
        corner_y += 35

    corner_y = 213                                                      #AI hand(player three, AI #2)
    corner_y -= (35 * int(len(players[2].hand)/2))
    for i in range(len(players[2].hand)):
        pygame.draw.rect(screen, WHITE, (400, corner_y, 100, 74), 2)
        pygame.draw.rect(screen, BLACK, (402, corner_y + 2, 97, 70))
        corner_y += 35

    corner_x = 213                                                      #This block is for the human player
    corner_x -= (35 * int(len(players[0].hand) / 2))
    for i in range(0, len(players[0].hand)):
        the_color = BLACK
        if players[0].hand[i][0] is None and (players[0].hand[i][1] == "W" or players[0].hand[i][1] == "+4"):
            the_color = BLACK
        elif players[0].hand[i][0] == "R":
            the_color = RED
        elif players[0].hand[i][0] == "B":
            the_color = BLUE
        elif players[0].hand[i][0] == "Y":
            the_color = YELLOW
        elif players[0].hand[i][0] == "G":
            the_color = GREEN
        pygame.draw.rect(screen, WHITE, (corner_x, 402, 74, 100), 2)
        pygame.draw.rect(screen, the_color, (corner_x + 2, 404, 70, 97))
        text = CARD_FONT.render(players[0].hand[i][1], 1, WHITE)
        screen.blit(text, (corner_x + 3, 350))
        corner_x += 35          #human hand

    pygame.draw.rect(screen, RED, (220, 10, 15, 15))
    pygame.draw.rect(screen, GREEN, (240, 10, 15, 15))
    pygame.draw.rect(screen, BLUE, (260, 10, 15, 15))
    pygame.draw.rect(screen, YELLOW, (280, 10, 15, 15))

    pygame.display.update()

def has_winner(players, player):
    if len(players[player].hand) < 1:
        pygame.time.delay(750)
        screen.fill((0, 0, 175))
        if player == 0:
            text = END_FONT.render("You have won!", 1, (255, 255, 255))
            screen.blit(text, (100, 250))
        elif player != 0:
            text = END_FONT.render("Player " + str(player + 1) + " has won!", 1, (255, 255, 255))
            screen.blit(text, (50, 250))
        pygame.display.update()
        pygame.time.delay(1750)
        return False
    return True

def play_game():
    run = True
    deck = gf.make_deck()[:]
    deck = gf.shuffle(deck)[:]

    player_hands, deck = gf.distribute(deck)[:]

    p_1 = playerFunctions(player_hands[0], False)
    p_2 = playerFunctions(player_hands[1], True)
    p_3 = playerFunctions(player_hands[2], True)

    players = [p_1, p_2, p_3]
    current_card = deck[0]
    deck.pop(0)
    used_cards = []
    player = 0
    direction = 1
    draw = 0

    color = current_card[0]

    update_screen(players, current_card, color)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        played, direction, next_player, draw, deck, color = (players[player]).has_playable(current_card, deck, draw, used_cards, direction, color)

        run = has_winner(players, player)

        player = player + (direction * next_player + 3)
        player = player % 3
        if len(played) != 0:
            current_card = played[:]
            used_cards.append(played)

        update_screen(players, current_card, color)


while True:
    play_game()

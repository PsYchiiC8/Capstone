import random
import Crazy_8s_util as gf
import pygame

pygame.init()
class playerFunctions:
    def __init__(self, hand, is_com):
        self.hand = hand
        self.is_com = is_com

    def draw_card(self, deck, used, need_draw=1):
        for i in range(0, need_draw):
            if len(deck) == 0:
                deck = used[:]
                deck = gf.shuffle(deck)
                used = []
            self.hand.append(deck[0])
            deck.pop(0)
        return deck, used

    def play_card_ai(self, direction, current_card, playable):         #this is for the non-human player(computer players), chose a card to play
        color = current_card[0]
        played = []
        next_player = 1
        if self.is_com == True:
            index = random.randint(0, (len(playable) - 1))
            played = playable[index]
            draw = 0
            for i in range(0, len(self.hand) - 1):
                if self.hand[i] == played:
                    self.hand.pop(i)
                    break
            if played[1] == "+2" or played[1] == "+4" or played[1] == "W":
                if played[1] == "+2":
                    draw = 2
                elif played[1] == "+4":
                    draw = 4
                    colors = ["R", "G", "B", "Y"]
                    color = colors[random.randint(0, len(colors) - 1)]
                elif played[1] == "W":
                    colors = ["R", "G", "B", "Y"]
                    color = colors[random.randint(0, len(colors) - 1)]
            elif played[1] == "R":
                direction *= -1
            elif played[1] == "S":
                next_player = 2
            return played, direction, next_player, draw, color

    def play_card_human(self, deck, used, current_card, direction, color):              #human player plays card
        played = []
        next_player = 1

        if self.is_com is False:
            run = True
            draw = 0
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        m_x, m_y = pygame.mouse.get_pos()
                        if m_y > 425:
                            bound_size = int((500 - (len(self.hand) * 35 + 40)) / 2)
                            lower_bound = bound_size
                            upper_bound = 500 - bound_size
                            if lower_bound < m_x < upper_bound:
                                index = int((m_x - bound_size) // 35)
                                if index >= len(self.hand):
                                    index -= 1
                                tentative = self.hand[index]
                                if (tentative[0] is None and (tentative[1] == "+4" or tentative[1] == "W")) or tentative[0] == current_card[0] or tentative[0] == color or tentative[1] == current_card[1]:
                                    played = self.hand[index]
                                    self.hand.pop(index)
                                    if played[1] == "+2" or played[1] == "+4" or played[1] == "W":
                                        if played[1] == "+2":
                                            draw = 2
                                        elif played[1] == "+4":
                                            draw = 4
                                            colors = ["R", "G", "B", "Y"]
                                            color = colors[random.randint(0, 3)]
                                        elif played[1] == "W":
                                            colors = ["R", "G", "B", "Y"]
                                            color = colors[random.randint(0, 3)]
                                    elif played[1] == "R":
                                        direction *= -1
                                    elif played[1] == "S":
                                        next_player = 2

                                    return played, direction, next_player, draw, color
                        elif (174 < m_x < 248) and (200 < m_y < 300):
                            self.draw_card(deck, used, 1)
                            run = False
            return played, direction, next_player, draw, color

    def has_playable(self, current_card, deck, need_draw, used, direction, color):
        played = []
        draw = 0
        playable = []
        next_player = 1

        for card in self.hand:
            if (card[0] == current_card[0]) or (card[1] == current_card[1]) or (card[1] == "+4") or (card[1] == "W"):
                playable.append(card)

        if (len(playable) == 0 and self.is_com == True):
            deck, used = self.draw_card(deck, used)
        elif need_draw != 0:
            deck, used = self.draw_card(deck, used, need_draw)
        elif self.is_com is False:
            played, direction, next_player, draw, color = self.play_card_human(deck, used, current_card, direction, color)
        elif len(playable) != 0 and self.is_com == True:
            played, direction, next_player, draw, color = self.play_card_ai(direction, current_card, playable)

        return played, direction, next_player, draw, deck, color

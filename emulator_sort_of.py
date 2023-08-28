import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Emulator")

def display_home():
    screen.fill((0, 0, 175))

    END_FONT = pygame.font.SysFont('courier', 20)

    pygame.draw.rect(screen, (255, 255, 255), (150, 150, 200, 75), 2)
    pygame.draw.rect(screen, (200, 200, 20), (152, 152, 197, 72))
    text = END_FONT.render("Crazy 8's", 1, (0, 0, 0))
    screen.blit(text, (200, 175))
    pygame.draw.rect(screen, (255, 255, 255), (150, 250, 200, 75), 2)
    pygame.draw.rect(screen, (200, 200, 20), (152, 252, 197, 72))
    text = END_FONT.render("TicTacToe", 1, (0, 0, 0))
    screen.blit(text, (200, 275))
    pygame.display.update()

def run_game():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if (150 < m_x < 350) and (150 < m_y < 225):
                    import Crazy_8s
                elif (150 < m_x < 350) and (250 < m_y < 325):
                    import TicTacToe
        display_home()


while True:
    run_game()
import pygame
import math
# Initializing Pygame
pygame.init()

# Screen
WIDTH = 500
ROWS = 3
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Images
X_IMAGE = pygame.transform.scale(pygame.image.load("X.png"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("O.png"), (150, 150))

# Fonts
END_FONT = pygame.font.SysFont('courier', 40)


def draw_grid():
    gap = WIDTH // ROWS

    # Starting points
    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap

        pygame.draw.line(screen, GRAY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(screen, GRAY, (0, x), (WIDTH, x), 3)


def initialize_grid():
    dis_to_cen = WIDTH // ROWS // 2

    # Initializing the array
    grid = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x = dis_to_cen * (2 * j + 1)
            y = dis_to_cen * (2 * i + 1)

            # Adding centre coordinates
            grid[i][j] = (x, y, "", True)

    return grid

def click(player, board):
    global images
    m_x, m_y = pygame.mouse.get_pos()
    x, y, char, can_play = board[int(m_y//(500/3))][int(m_x//(500/3))]

    if player == "X":  # If it's X's turn
        images.append((x, y, X_IMAGE))
        board[int(m_y//(500/3))][int(m_x//(500/3))] = (x, y, 'X', False)
    elif player == "O":  # If it's O's turn
        images.append((x, y, O_IMAGE))
        board[int(m_y//(500/3))][int(m_x//(500/3))] = (x, y, 'O', False)

def change_player(player):
    if player == "X":
        return "O"
    return "X"

def playable(grid):
    # Mouse position
    m_x, m_y = pygame.mouse.get_pos()

    x, y, char, can_play = grid[int(m_y//(500/3))][int(m_x//(500/3))]
    return can_play

# Checking if someone has won by calling other functions that check certain ways to win
def has_won(player, grid):
    if check_vertical(player, grid) or check_horizontal(player, grid) or check_diagonal(player, grid):
        return True

    return False

def check_horizontal(player, grid):
    """
    This function checks if a player has won horizontally.
    """
    for i in range(3):
        if ((grid[i][0][2] == player) and (grid[i][1][2] == player) and (grid[i][2][2] == player)):
            return True
    return False

def check_vertical(player, grid):
    """
    This function checks if a player has won vertically.
    """
    for i in range(3):
        if (grid[0][i][2] == player) and (grid[1][i][2] == player) and (grid[2][i][2] == player):
            return True

    return False


def check_diagonal(player, grid):
    """
    This function checks if a player has won diagonally.
    """
    if (grid[0][0][2] == player and grid[1][1][2] == player and grid[2][2][2] == player) or (grid[0][2][2] == player and grid[1][1][2] == player and grid[2][0][2] == player):
        return True

    return False


def has_drawn(grid):
    for i in range(3):
        for j in range(3):
            x, y, char, can_play = grid[i][j]
            if char == '':
                return False
    return True


def display_message(content):
    pygame.time.delay(200)
    screen.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    screen.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(1250)


def update_screen():
    screen.fill(WHITE)
    draw_grid()

    # Drawing X's and O's
    for image in images:
        x, y, IMAGE = image
        screen.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()


def play_game():
    global images, draw

    images = []
    draw = False

    run = True

    player = "O"

    board = initialize_grid()
    draw_grid()
    update_screen()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playable(board):
                    player = change_player(player)
                    click(player, board)
                    update_screen()
                    if has_won(player, board):
                        display_message("Player " + player + " has won")
                        run = False
                    if has_drawn(board) and run:
                        display_message("It's a draw")
                        run = False

while True:
    play_game()

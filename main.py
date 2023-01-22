import pygame
from settings import *
from sudoku import *

class Game:
    def __init__(self):
        self.difficulty = float(input('Please enter difficulty (betweeen 0 to 1): '))
        self.sudoku = Sudoku()
        self.board = self.sudoku.generate_puzzle(scale=self.difficulty)
        pygame.init()
        pygame.display.set_caption('Sudoku')
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.font = pygame.font.SysFont('robotoregular', int(CELLSIZE // 2))
        self.completed_board = []
        self.mouse_position = (0,0)
        self.clock = pygame.time.Clock()
        self.hover_rect = None
        self.hover_sound = pygame.mixer.Sound(hover_sound)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    return
                if event.key == pygame.K_F11:
                    # INITIALISE SUDOKU PARAMETERS
                    self.board = self.sudoku.generate_puzzle(scale=self.difficulty)
                    print(self.board)
                if event.key == pygame.K_F12:
                    self.board = self.sudoku.single_solve(self.board)
                    print(self.board)

    def update(self):
        pygame.display.update()

    def run(self):
        while self.running:
            self.events()
            self.draw_window()
            self.draw_grid()
            self.mouse_position = pygame.mouse.get_pos()
            self.hover_cell()
            self.draw_num()
            self.update()
        sys.exit()
        pygame.quit()

    def draw_window(self):
        self.window.fill(WHITE)

    def draw_grid(self):
        # Draw Outer Border
        pygame.draw.rect(self.window, BLACK, (GRID_POS[0], GRID_POS[1], GRID_WIDTH, GRID_HEIGHT), outer_thickness)

        # Draw all cells
        for count in range(9):
            if count == 0:
                continue
            if count == 3 or count == 6:
                pygame.draw.line(self.window, BLACK, (GRID_POS[0] + count * CELLSIZE, GRID_POS[1]),
                                 (GRID_POS[0] + count * CELLSIZE, GRID_POS[1] + GRID_HEIGHT), 3)
                pygame.draw.line(self.window, BLACK, (GRID_POS[0], GRID_POS[1] + count * CELLSIZE),
                                 (GRID_POS[0] + GRID_WIDTH, GRID_POS[1] + count * CELLSIZE), 3)
            else:
                pygame.draw.line(self.window, BLACK, (GRID_POS[0] + count * CELLSIZE, GRID_POS[1]),
                                 (GRID_POS[0] + count * CELLSIZE, GRID_POS[1] + GRID_HEIGHT), 1)
                pygame.draw.line(self.window, BLACK, (GRID_POS[0], GRID_POS[1] + count * CELLSIZE),
                                 (GRID_POS[0] + GRID_WIDTH, GRID_POS[1] + + count * CELLSIZE), 1)

    def get_mousePosition(self):
        if self.mouse_position[0] < GRID_POS[0] + 3 or self.mouse_position[0] > GRID_POS[0] + GRID_WIDTH - 3:
            return False
        elif self.mouse_position[1]  < GRID_POS[1] + 3 or self.mouse_position[1] > GRID_POS[1] + GRID_HEIGHT - 3:
            return False
        else:
            return ((self.mouse_position[0] - GRID_POS[0]) // CELLSIZE, (self.mouse_position[1] - GRID_POS[1]) // CELLSIZE)

    def draw_highlight(self,mouse_position):
        pygame.draw.rect(self.window, LIGHTBLUE, ( (mouse_position[0] * CELLSIZE) + GRID_POS[0] + 2, (mouse_position[1] * CELLSIZE) + GRID_POS[1] + 2, CELLSIZE - 3,CELLSIZE - 3))
        return pygame.draw.rect(self.window, LIGHTBLUE, ( (mouse_position[0] * CELLSIZE) + GRID_POS[0] + 2, (mouse_position[1] * CELLSIZE) + GRID_POS[1] + 2, CELLSIZE - 3,CELLSIZE - 3))

    def draw_num(self):
        for i in range(0, len(self.board[0])):
            for j in range(0, len(self.board[0])):
                if (0 < self.board[i][j] < 10):
                    value = self.font.render(str(self.board[i][j]), True, BLACK)
                    self.window.blit(value, (GRID_POS[0] + j * CELLSIZE + CELLSIZE / 4 + 12, i * CELLSIZE + GRID_POS[1] + CELLSIZE / 3))

    def hover_cell(self):
        if self.get_mousePosition():
            self.draw_highlight(self.get_mousePosition())
            if self.hover_rect != self.draw_highlight(self.get_mousePosition()):
                self.hover_rect = self.draw_highlight(self.get_mousePosition())
                self.hover_sound.play()
        else:
            self.hover_rect = None

if __name__ == "__main__":
    game = Game()
    game.run()

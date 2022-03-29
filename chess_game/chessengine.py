import pygame as p
from gamestate import GameState

WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
BUTTONS = []
FONT_SIZE = 30

def load_images(font, screen):
    #load in pieces
    pieces = ["Bb", "Bk", "Bn", "Bp", "Bq", "Br",
              "Wb", "Wk", "Wn", "Wp", "Wq", "Wr"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("chess_game/images/" + piece + ".png"),
                                         (SQUARE_SIZE, SQUARE_SIZE))

    #load in menu buttons
    button_surface = p.transform.scale(p.image.load("chess_game/images/green_button.png"), (200, 100))
    white = Button("W", font, screen, button_surface, 100, 250, "Play as White")
    black = Button("B", font, screen, button_surface, 415, 250, "Play as Black")
    BUTTONS.append(white)
    BUTTONS.append(black)
    

def main():
    p.init()
    game_state = GameState()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Chess vs Computer")
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    font = p.font.SysFont("cambria", FONT_SIZE)
    load_images(font, screen)

    board = game_state.get_board()
    selected_square = ()
    player_clicks = []
    running = True
    game_active = False
    menu_screen = True

    while running:
        #create three game states: menu screen, game over, and in game
        if menu_screen:
            draw_board(screen)
            #same code as handling buttons, make into function
            for e in p.event.get():
                if e.type == p.MOUSEBUTTONDOWN:
                    x, y = p.mouse.get_pos()
                    for button in BUTTONS:
                        result = button.check_input(x, y)
                        if result:
                            print(result)
                            game_state.reset(result, 1)
                            menu_screen = False
                            game_active = True
                            break

            for button in BUTTONS:
                button.update()
            clock.tick(MAX_FPS)
            p.display.flip()

        if game_active:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos()
                    col = location[0] // SQUARE_SIZE
                    row = location[1] // SQUARE_SIZE
                    if selected_square == (row, col):
                        selected_square = ()
                        player_clicks = []
                    else:
                        selected_square = (row, col)
                        #QOL piece selection: nested if statements to allow for castling
                        if (board.is_occupied(row, col) and 
                            board.get_piece_color(row, col) == game_state.get_turn()):
                            if len(player_clicks) == 1:
                                start_row, start_column = player_clicks[0]
                                king_symbol = game_state.get_turn() + "k"
                                if board.get_square(start_row, start_column).get_symbol() == king_symbol:
                                    player_clicks.append(selected_square)
                                else:
                                    player_clicks = [selected_square]
                                    print(player_clicks) 
                            else:
                                player_clicks = [selected_square]
                                print(player_clicks)
                        elif len(player_clicks) == 1:
                            player_clicks.append(selected_square)
                            print(player_clicks)
                        
                    if len(player_clicks) == 2:
                        start_row, start_column = player_clicks[0][0], player_clicks[0][1]
                        end_row, end_column = player_clicks[1][0], player_clicks[1][1]
                        piece = board.get_square(start_row, start_column)
                        if game_state.log_move(piece, start_row, start_column, end_row, end_column):
                            if game_state.is_stalemate():
                                print("stalemate")
                                game_active = False
                            if game_state.is_checkmate():
                                if game_state.get_turn() == "W":
                                    print("Black wins by checkmate")
                                else:
                                    print("White wins by checkmate")
                                game_active = False
                            elif game_state.is_check():
                                print("check!")

                        selected_square = ()
                        player_clicks = []

            draw_game_state(screen, game_state, selected_square)
            clock.tick(MAX_FPS)
            p.display.flip()
        else: #game has ended
            for e in p.event.get():
                if e.type == p.MOUSEBUTTONDOWN:
                    x, y = p.mouse.get_pos()
                    for button in BUTTONS:
                        result = button.check_input(x, y)
                        if result:
                            print(result)
                            game_state.reset(result, 1)
                            menu_screen = False
                            game_active = True
                            break

            for button in BUTTONS:
                button.update()
            clock.tick(MAX_FPS)
            p.display.flip()

def highlight_squares(screen, game_state, selected_square):
    #problem: this is being called MAX_FPS times a second, which generates legal moves every time
    #idk if this will be a problem for AI, maybe adjust in future
    if selected_square:
        row, column = selected_square
        board = game_state.get_board()
        piece = board.get_square(row, column)
        color = game_state.get_turn()
        if not piece or piece.get_color() != color:
            return
        prev_move = game_state.get_prev_move()
        color = game_state.get_turn()
        king = board.get_king(color)

        legal_moves = piece.generate_legal_moves(king, prev_move)
        s = p.Surface((SQUARE_SIZE,SQUARE_SIZE))
        s.set_alpha(100)
        s.fill(p.Color('blue'))
        screen.blit(s, (column * SQUARE_SIZE, row * SQUARE_SIZE))

        s.fill(p.Color('yellow'))
        for end_row, end_column in legal_moves:
            screen.blit(s, (end_column * SQUARE_SIZE, end_row * SQUARE_SIZE))

def draw_game_state(screen, game_state, selected_square):
    draw_board(screen)
    highlight_squares(screen, game_state, selected_square)
    draw_pieces(screen, game_state.get_board())

def draw_board(screen):
    #draws board based on screen coordinates
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(0, DIMENSION):
        for column in range(0, DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE,
                                              SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board):
    #draws pieces based on coordinates of screen
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            if board.is_occupied(row, column):
                piece = board.get_square(row, column)
                symbol = piece.get_symbol()
                screen.blit(IMAGES[symbol], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE,
                                                   SQUARE_SIZE, SQUARE_SIZE))

class Button():
    def __init__(self, color, font, screen, image, x, y, text_input):
        self.color = color
        self.screen = screen
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.text_input = text_input
        self.text = font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center = (self.x, self.y))

    def update(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)

    def check_input(self, x, y):
        if x in range(self.rect.left, self.rect.right) and y in range(self.rect.top, self.rect.bottom):
            return self.color
        return None
if __name__ == "__main__":
    main()



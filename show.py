import arcade
import logic

WIDTH = 250
HEIGHT = 250

SIZE = 3
MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * SIZE
SCREEN_HEIGHT = (HEIGHT + MARGIN) * SIZE
SCREEN_TITLE = "Tic-tac-toe"

class Window(arcade.Window):
    def __init__(self, width, height, title):
        arcade.set_background_color(arcade.color.BLACK)
        super().__init__(width, height, title)
        self.grid_sprite_list = [arcade.SpriteList() for _ in range(SIZE)]
        for row in range(SIZE):

            for col in range(SIZE):
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.BLACK)
                sprite.center_x = MARGIN * col + col * WIDTH + WIDTH / 2
                sprite.center_y = MARGIN * row + row * WIDTH + WIDTH / 2
                
                self.grid_sprite_list[row].append(sprite)
        self.tictactoe = logic.tictactoe()
        self.result = None

            
    def reset(self):
        self.grid_sprite_list = [arcade.SpriteList() for _ in range(SIZE)]
        for row in range(SIZE):
            for col in range(SIZE):
                sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, arcade.color.BLACK)
                sprite.center_x = MARGIN * col + col * WIDTH + WIDTH / 2
                sprite.center_y = MARGIN * row + row * WIDTH + WIDTH / 2
                
                self.grid_sprite_list[row].append(sprite)
        self.tictactoe = logic.tictactoe()
        self.result = None
    def on_draw(self):
        arcade.start_render()

        for row in self.grid_sprite_list:
            row.draw()

        
        arcade.draw_rectangle_filled(250, 385, MARGIN, SCREEN_HEIGHT, arcade.color.WHITE)
        arcade.draw_rectangle_filled(505, 385, MARGIN, SCREEN_HEIGHT, arcade.color.WHITE)
        arcade.draw_rectangle_filled(385, 250, SCREEN_WIDTH, MARGIN, arcade.color.WHITE)
        arcade.draw_rectangle_filled(385, 505, SCREEN_WIDTH, MARGIN, arcade.color.WHITE)
        if self.result is not None:
            if self.result == "X":

                arcade.draw_rectangle_filled(382.5, 380, 700, 100, color = arcade.color.BLACK)
                arcade.draw_text("You have WON the game!", 55, 345, color = arcade.color.WHITE, align="center", font_size=45, font_name=("Lucida Console", "helvetica"))
            if self.result == "O":
                arcade.draw_rectangle_filled(382.5, 380, 700, 100, color = arcade.color.BLACK)
                arcade.draw_text("You have LOST the game.", 55, 345, color = arcade.color.WHITE, align="center", font_size=45, font_name=("Lucida Console", "helvetica"))
            if self.result == "tie":
                arcade.draw_rectangle_filled(382.5, 380, 800, 100, color = arcade.color.BLACK)
                arcade.draw_text("The game has ended in a TIE!", 7, 345, color = arcade.color.WHITE, align="center", font_size=45, font_name=("Lucida Console", "helvetica"))
    #pylint: disable = attribute-defined-outside-init
    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.R:
            self.reset()
        if symbol == arcade.key.Q:
            print("\nExit requested by user\n")
            self.close()
    def on_mouse_press(self, x, y, button, modifiers):
        if self.result is None:

            column = int(x // (WIDTH + MARGIN))
            row = int(y // (HEIGHT + MARGIN))
            xSprite = arcade.Sprite("x.jpeg", image_width = WIDTH, image_height = HEIGHT)
            xSprite.center_x = MARGIN * column + column * WIDTH + WIDTH / 2

            xSprite.center_y = MARGIN * row + row * WIDTH + WIDTH / 2
            if self.tictactoe.grid[row][column] == " ":
                self.grid_sprite_list[row][column] = xSprite
                step = self.tictactoe.step((row, column))
                if step == "check result": 
                    self.result = logic.check(self.tictactoe.grid)
                else: 
                    ay, ax = step
                    oSprite = arcade.Sprite("o.jpeg", image_width = WIDTH, image_height = HEIGHT)
                    oSprite.center_x = MARGIN * ax + ax * WIDTH + WIDTH / 2

                    oSprite.center_y = MARGIN * ay + ay * WIDTH + WIDTH / 2
                    self.grid_sprite_list[ay][ax] = oSprite
                    self.result = logic.check(self.tictactoe.grid)


Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()

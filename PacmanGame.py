import arcade

#קבועים
SCREEN_WIDTH= 800
SCREEN_HEIGHT= 600
SCREEN_TITLE= "My First Pacman Game"
TILE_SIZE= 32
MAP_LEVEL = [
    "###########",
    "#PCCCCGCCC#",
    "#CCCCCCCCC#",
    "###########"
]

class Wall(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_rectangle_texture(TILE_SIZE, TILE_SIZE, arcade.color.BLUE)
        self.width = TILE_SIZE
        self.height = TILE_SIZE

class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__()
        size = TILE_SIZE // 2
        self.texture = arcade.make_circle_texture(size, arcade.color.YELLOW)
        self.width = size
        self.height = size

class Ghost(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE, arcade.color.RED)
        self.width = TILE_SIZE
        self.height = TILE_SIZE

class Pacman(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE, arcade.color.YELLOW)
        self.width = TILE_SIZE
        self.height = TILE_SIZE

class PacmanGame(arcade.View):

    def __init__(self):
        super().__init__()

        self.wall_list= arcade.SpriteList()
        self.coin_list= arcade.SpriteList()
        self.ghost_list= arcade.SpriteList()
        self.player_list= arcade.SpriteList()
        self.player= None
        self.game_over= False
        self.background_color= arcade.color.BLACK
        self.start_x= 0
        self.start_y= 0
        self.score= 0
        self.lives= 3

    def setup(self):
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.game_over = False
        rows= len(MAP_LEVEL)

        for row_idx, row in enumerate(MAP_LEVEL):
            for col_idx, cell in enumerate(row):
                x = col_idx * TILE_SIZE + TILE_SIZE / 2
                y = (rows - row_idx - 1) * TILE_SIZE + TILE_SIZE / 2
                if cell== "#":
                    wall= Wall()
                    wall.center_x= x
                    wall.center_y= y
                    self.wall_list.append(wall)
                elif cell== "C":
                    coin= Coin()
                    coin.center_x= x
                    coin.center_y= y
                    self.coin_list.append(coin)
                elif cell== "G":
                    ghost= Ghost()
                    ghost.center_x= x
                    ghost.center_y= y
                    self.ghost_list.append(ghost)
                elif cell== "P":
                    self.player= Pacman()
                    self.player.center_x= x
                    self.player.center_y= y
                    self.player_list.append(self.player)
                    self.start_x= x
                    self.start_y= y


    def on_draw(self):
        arcade.start_render()

        self.wall_list.draw()
        self.coin_list.draw()
        self.ghost_list.draw()
        self.player_list.draw()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT -30, arcade.color.WHITE, 16)
        arcade.draw_text(f"Lives: {self.lives}", 10, SCREEN_HEIGHT -55, arcade.color.WHITE, 16)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.RED, 40)

def main():
    window= arcade.Window
import arcade

#קבועים
SCREEN_WIDTH= 800
SCREEN_HEIGHT= 600
SCREEN_TITLE= "My First Pacman Game"
TILE_SIZE= 32
MAP_LEVEL = [
"#########################",
"#PCCCCCCCCCC##CCCCCCCCCC#",
"#C####C#####C##C#####C###",
"#C####C#####C##C#####C###",
"#CCCCCCCCCCCCCCCCCCCCCCC#",
"#C####C##C########C##C###",
"#CCCCCC##CCCC##CCCC##CCC#",
"######C#####C##C#####C###",
"#CCCCCCCC##CCCC##CCCCCCC#",
"#C#######C#G##C#C#########",
"#CCCCCCCC##CCCC##CCCCCCC#",
"######C#####C##C#####C###",
"#CCCCCC##CCCC##CCCC##CCC#",
"#C####C##C########C##C###",
"#CCCCCCCCCCCCCCCCCCCCCCC#",
"#C####C#####C##C#####C###",
"#CCCC##CCCCCCCCCCCC##CCC#",
"#########################"
]




class Wall(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.texture = arcade.make_soft_square_texture(TILE_SIZE, arcade.color.BLUE)
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.center_x=x
        self.center_y=y


class Coin(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        size = TILE_SIZE // 2
        self.texture = arcade.make_circle_texture(size, arcade.color.YELLOW)
        self.width = size
        self.height = size
        self.center_x=x
        self.center_y=y


class Ghost(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE, arcade.color.RED)
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.center_x=x
        self.center_y=y


class Pacman(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.texture = arcade.make_circle_texture(TILE_SIZE, arcade.color.YELLOW)
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.center_x=x
        self.center_y=y


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
                    wall= Wall(x,y)
                    self.wall_list.append(wall)

                elif cell== "C":
                    coin= Coin(x,y)
                    self.coin_list.append(coin)

                elif cell== "G":
                    ghost= Ghost(x,y)
                    self.ghost_list.append(ghost)

                elif cell== "P":
                    self.player= Pacman(x,y)
                    self.player_list.append(self.player)
                    self.start_x= x
                    self.start_y= y


    def on_draw(self):
        self.clear()
        self.wall_list.draw()
        self.coin_list.draw()
        self.ghost_list.draw()
        self.player_list.draw()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT -30, arcade.color.WHITE, 16)
        arcade.draw_text(f"Lives: {self.lives}", 10, SCREEN_HEIGHT -55, arcade.color.WHITE, 16)

        if self.game_over:
            arcade.draw_text("Game Over", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.RED, 40)


def main():
    window= arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game= PacmanGame()
    window.show_view(game)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()

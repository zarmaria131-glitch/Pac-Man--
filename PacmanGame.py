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
"#C######CC#G##C#CC########",
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
        size = TILE_SIZE // 4
        self.texture = arcade.make_circle_texture(size, arcade.color.YELLOW)
        self.width = size
        self.height = size
        self.center_x=x
        self.center_y=y


class Ghost(arcade.Sprite):
    def __init__(self,x,y,texture):
        super().__init__()
        self.texture= texture
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.center_x=x
        self.center_y=y


class Pacman(arcade.Sprite):
    def __init__(self,x,y,textures):
        super().__init__()
        self.textures= textures
        self.texture= self.textures[0]
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.center_x=x
        self.center_y=y
        self.anim_time= 0
        self.frame= 0

    def update_animation(self,delta_time= 1/60):
        self.anim_time+= delta_time
        if self.anim_time >= 0.15:
            self.anim_time= 0
            self.frame= (self.frame + 1) % 2
            self.texture= self.textures[self.frame]


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

    def load_textures(self):
        self.textures= [arcade.load_texture("assets/pacmanclose-removebg-preview.png"),
        arcade.load_texture("assets/pacmanopen-removebg-preview.png")]
        self.ghost_texture= arcade.load_texture("assets/redghost.png")

    def setup(self):
        self.load_textures()
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
                    ghost= Ghost(x,y,self.ghost_texture)
                    self.ghost_list.append(ghost)

                elif cell== "P":
                    self.player= Pacman(x,y,self.textures)
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

    def on_update(self,delta_time):
        if self.player:
            old_x = self.player.center_x
            old_y = self.player.center_y

            self.player.center_x += self.player.change_x
            self.player.center_y += self.player.change_y

            hit_list= arcade.check_for_collision_with_list(self.player, self.wall_list)

            if hit_list:
                self.player.center_x = old_x
                self.player.center_y = old_y

        for ghost in self.ghost_list:
            old_x = ghost.center_x
            old_y = ghost.center_y

            ghost.center_x += ghost.change_x
            ghost.center_y += ghost.change_y

            hit_list= arcade.check_for_collision_with_list(ghost, self.wall_list)

            if hit_list:
                ghost.center_x = old_x
                ghost.center_y = old_y

        self.player_list.update_animation(delta_time)


def main():
    window= arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game= PacmanGame()
    window.show_view(game)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()

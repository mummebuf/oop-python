import arcade
from models import World, Player
SCREEN_WIDTH = 840
SCREEN_HEIGHT = 600


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)


    def draw(self):
        self.sync_with_model()
        super().draw()


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.world = World(width, height)

        self.player_sprite = ModelSprite('images/wolf.png',model=self.world.player)

        self.end_sprites = []
        for end in self.world.ends:
            self.end_sprites.append(ModelSprite('images/warp.png',model=end))

        self.wall_sprites = []
        for wall in self.world.wall:
            self.wall_sprites.append(ModelSprite('images/block.png',model=wall))

        self.coin_texture = arcade.load_texture('images/meat.png')

        self.gameover_texture = arcade.load_texture('images/meat.png')


    def draw_coins(self, coins,player):
            for c in coins:
                if not c.is_collected:
                    arcade.draw_texture_rectangle(c.x, c.y, 40, 40,self.coin_texture)


    def on_draw(self):
        arcade.start_render()
        self.draw_coins(self.world.coins,self.world.player)
        self.player_sprite.draw()
        self.enemy_sprites =[]
        for enemy in self.world.enemies:
            self.enemy_sprites.append(ModelSprite('images/pig.png',model=enemy))

        for sprite in self.enemy_sprites:
            sprite.draw()

        for sprite in self.wall_sprites:
            sprite.draw()

        for sprite in self.end_sprites:
            sprite.draw()

        if(self.world.GAMEOVER == 0):
            arcade.draw_text(str(self.world.score),750,550,arcade.color.WHITE, 20)
        else:
            arcade.draw_text(str(0),750,550,arcade.color.WHITE, 20)

        if self.world.GAMEOVER == 1 and self.world.WIN == 0:
            arcade.draw_text("GAMEOVER",340,550,arcade.color.WHITE, 20)

        elif self.world.WIN == 1 and self.world.GAMEOVER == 0:
            arcade.draw_text("YOU WIN",375,570,arcade.color.WHITE, 15)
            arcade.draw_text("SCORE " + str(self.world.score),370,550,arcade.color.WHITE, 15)

    def animate(self, delta):
        self.world.animate(delta)


    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)


if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

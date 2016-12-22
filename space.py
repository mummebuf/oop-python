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

        # self.enemy_sprite = ModelSprite('images/pacman.png',model=self.world.enemy)

        self.enemy_sprites =[]
        for enemy in self.world.enemies:
            self.enemy_sprites.append(ModelSprite('images/pig.png',model=enemy))

        self.wall_sprites = []
        for wall in self.world.wall:
            self.wall_sprites.append(ModelSprite('images/wall.png',model=wall))

        self.coin_texture = arcade.load_texture('images/dot.png')


    def draw_coins(self, coins,player):
            for c in coins:
                if not c.is_collected:
                    arcade.draw_texture_rectangle(c.x, c.y, 40, 40,self.coin_texture)

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()

        # self.enemy_sprite.draw()
        for sprite in self.enemy_sprites:
            sprite.draw()

        for sprite in self.wall_sprites:
            sprite.draw()

        self.draw_coins(self.world.coins,self.world.player)

        arcade.draw_text(str(self.world.score),750,550,arcade.color.WHITE, 20)


    def animate(self, delta):
        self.world.animate(delta)


    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)


if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

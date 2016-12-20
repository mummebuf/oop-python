import arcade
from models import World, Ship
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

        self.ship_sprite = ModelSprite('images/ship.png',model=self.world.ship)

        # self.wall_sprite = ModelSprite('images/wall.png',model=self.world.wall)
        #
        # self.coin_sprite = ModelSprite('images/dot.png',model=self.world.coin)

        self.wall_sprites = []
        for wall in self.world.wall:
            self.wall_sprites.append(ModelSprite('images/wall.png',model=wall))

        self.coin_sprites = []
        for coin in self.world.coin:
            self.wall_sprites.append(ModelSprite('images/dot.png',model=coin))

    def on_draw(self):
        arcade.start_render()
        self.ship_sprite.draw()

        for sprite in self.wall_sprites:
            sprite.draw()

        for sprite in self.coin_sprites:
            sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)
# self.ship_sprite.set_position(self.world.ship.x, self.world.ship.y)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

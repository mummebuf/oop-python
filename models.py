import arcade.key

# class Ship:
#     DIR_UP = 0
#     DIR_DOWN = 1
#     DIR_LEFT = 2
#     DIR_RIGHT = 3
#
#     def __init__(self,world, x, y):
#         self.world = world
#         self.x = x
#         self.y = y
#         self.direction = Ship.DIR_DOWN
#
#     def direction_up(self):
#         self.direction = Ship.DIR_UP
#
#     def direction_down(self):
#         self.direction = Ship.DIR_DOWN
#
#     def direction_left(self):
#         self.direction = Ship.DIR_LEFT
#
#     def direction_right(self):
#         self.direction = Ship.DIR_RIGHT
#
#     def animate(self, delta):
#         if self.direction == Ship.DIR_UP:
#             if self.y > self.world.height:
#                 self.y = 0
#             self.y += 5
class Ship():
    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1
    DONE = 0
    DELTA_X = 0
    DELTA_Y = 0

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Ship.DIR_VERTICAL

    # def direction_up(self):
    #     # if Ship.done == 0:
    #     # while (Ship.done==0):
    #     self.y += self.world.speed
    #         # self.ship.direction_up()

    def direction_left(self):
        Ship.DELTA_Y = 1

            # self.ship.direction_up()

    def done(self):
        Ship.DELTA_X = 0
        Ship.DELTA_Y = 0

    def animate(self, delta):
        if self.x < self.world.width:
            self.x += Ship.DELTA_X * self.world.speed
        if self.y < self.world.height:
            self.y += Ship.DELTA_Y * self.world.speed



class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.ship = Ship(self,100, 100)
        self.speed = 1

    def animate(self, delta):
        self.ship.animate(delta)

    # def on_key_press(self, key, key_modifiers):
    #     if key == arcade.key.SPACE:
    #         while self.ship.DONE ==0:
    #              self.ship.direction_up()
    #         # self.ship.switch_direction()
    #

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ship.direction_left()

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ship.done()


    # def on_key_press(self, key, key_modifiers):
    #     if key == arcade.key.SPACE:
    #         self.ship.direction_up()
    #     if key == arcade.key.A:
    #         self.ship.left()
    #     if key == arcade.key.S:
    #         self.ship.down()
    #     if key == arcade.key.D:
    #         self.ship.right()

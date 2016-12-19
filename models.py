import arcade.key

class Ship():
    DELTA_X = 0
    DELTA_Y = 0

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def direction_left(self):
        Ship.DELTA_X = -1
        # Ship.DELTA_Y = 0

    def direction_right(self):
        Ship.DELTA_X = 1
        # Ship.DELTA_Y = 0

    def direction_down(self):
        # Ship.DELTA_X = 0
        Ship.DELTA_Y = -1

    def direction_up(self):
        # Ship.DELTA_X = 0
        Ship.DELTA_Y = 1

    def done(self):
        Ship.DELTA_X = 0
        Ship.DELTA_Y = 0

    def animate(self, delta):
        if self.x <= self.world.width and self.x >= 0:
            self.x += Ship.DELTA_X * self.world.speed

        if self.x > self.world.width:
            self.x = self.world.width

        if self.x < 0:
            self.x = 0

        if self.y <= self.world.height and self.y >=0:
            self.y += Ship.DELTA_Y * self.world.speed

        if self.y > self.world.width:
            self.y = self.world.width

        if self.y < 0:
            self.y = 0

class Maze:
    MAP = [ "xxxxxxxxxxxxxxxxxxxx",
            "x..................x",
            "x.xxx.xxx..xxx.xxx.x",
            "x.x...x......x...x.x",
            "x.x.xxx.xxxx.xxx.x.x",
            "x.x.x..........x.x.x",
            "x.....xxx..xxx.....x",
            "x.x.x..........x.x.x",
            "x.x.xxx.xxxx.xxx.x.x",
            "x.x...x......x...x.x",
            "x.xxx.xxx..xxx.xxx.x",
            "x..................x",
            "xxxxxxxxxxxxxxxxxxxx" ]
    height = len(MAP)
    width  = len(MAP[0])

class Wall:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

class Coin:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y





class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze= Maze
        self.speed = 10
        self.ship = Ship(self,100, 100)
        self.wall = []
        self.coin = []
        for r in range(self.maze.height):
            c = 0
            for letter in self.maze.MAP[r]:
                    x = c * 40
                    y = self.height - (r * 40) - 40
                    if letter == "x":
                        wall = Wall(self,x,y)
                        self.wall.append(wall)
                    else:
                        coin = Coin(self,x,y)
                        self.coin.append(coin)
                    c += 1

        # print("xex",self.wall)
        # print("yes",self.coin)

    def animate(self, delta):
        self.ship.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.A:
            self.ship.direction_left()
        if key == arcade.key.W:
            self.ship.direction_up()
        if key == arcade.key.D:
            self.ship.direction_right()
        if key == arcade.key.S:
            self.ship.direction_down()

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.A:
            self.ship.done()
        if key == arcade.key.W:
            self.ship.done()
        if key == arcade.key.D:
            self.ship.done()
        if key == arcade.key.S:
            self.ship.done()

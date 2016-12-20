import arcade.key

class Player():
    DELTA_X = 0
    DELTA_Y = 0
    NEXT_DELTA_X = 0
    NEXT_DELTA_Y = 0

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def isAtCenter(self):
        return (self.x % 40) == 0 and (self.y % 40) == 0

    def setNextDirectionUp(self):
        Player.NEXT_DELTA_X = 0
        Player.NEXT_DELTA_Y = 1

    def setNextDirectionDown(self):
        Player.NEXT_DELTA_X = 0
        Player.NEXT_DELTA_Y = -1

    def setNextDirectionRight(self):
        Player.NEXT_DELTA_X = 1
        Player.NEXT_DELTA_Y = 0

    def setNextDirectionLeft(self):
        Player.NEXT_DELTA_X = -1
        Player.NEXT_DELTA_Y = 0
        
    def setNextDirectionDone(self):
        Player.NEXT_DELTA_X = 0
        Player.NEXT_DELTA_Y = 0

    # def direction_left(self):
    #     Player.DELTA_X = -1
    #     Player.DELTA_Y = 0
    #
    # def direction_right(self):
    #     Player.DELTA_X = 1
    #     Player.DELTA_Y = 0
    #
    # def direction_down(self):
    #     Player.DELTA_X = 0
    #     Player.DELTA_Y = -1
    #
    # def direction_up(self):
    #     Player.DELTA_X = 0
    #     Player.DELTA_Y = 1
    #
    # def done(self):
    #     Player.DELTA_X = 0
    #     Player.DELTA_Y = 0

    def animate(self, delta):
        if self.isAtCenter():
            Player.DELTA_X = Player.NEXT_DELTA_X
            Player.DELTA_Y = Player.NEXT_DELTA_Y
        if self.x <= self.world.width and self.x >= 0:
            self.x += Player.DELTA_X * self.world.speed

        if self.x > self.world.width:
            self.x = self.world.width

        if self.x < 0:
            self.x = 0

        if self.y <= self.world.height and self.y >=0:
            self.y += Player.DELTA_Y * self.world.speed

        if self.y > self.world.height:
            self.y = self.world.height

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

    def hasWallAt(r,c):
        return Maze.MAP[r] [c] == "x"

    def hasCoinAt(r,c):
        return Maze.MAP[r] [c] == "."

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
        self.player = Player(self,80, 80)
        self.wall = []
        self.coin = []
        for r in range(self.maze.height):
            c = 0
            for letter in self.maze.MAP[r]:
                    x = (c+1) * 40
                    y = self.height - (r * 40) - 80
                    if self.maze.hasWallAt(r,c):
                        wall = Wall(self,x,y)
                        self.wall.append(wall)
                    if self.maze.hasCoinAt(r,c):
                        coin = Coin(self,x,y)
                        self.coin.append(coin)
                    c += 1

        # print("xex",self.wall)
        # print("yes",self.coin)

    def animate(self, delta):
        self.player.animate(delta)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.A:
            self.player.setNextDirectionLeft()
        if key == arcade.key.W:
            self.player.setNextDirectionUp()
        if key == arcade.key.D:
            self.player.setNextDirectionRight()
        if key == arcade.key.S:
            self.player.setNextDirectionDown()
        if key == arcade.key.SPACE:
            self.player.setNextDirectionDone()

    # def on_key_release(self, key, key_modifiers):
    #     if key == arcade.key.A:
    #         self.player.done()
    #     if key == arcade.key.W:
    #         self.player.done()
    #     if key == arcade.key.D:
    #         self.player.done()
    #     if key == arcade.key.S:
    #         self.player.done()

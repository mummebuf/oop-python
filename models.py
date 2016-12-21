import arcade.key
COIN_MARGIN = 5
COIN_HIT_MARGIN = 5
class Player():
    DELTA_X = 0
    DELTA_Y = 0
    NEXT_DELTA_X = 0
    NEXT_DELTA_Y = 0
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.r = (600 - 80 - self.y)//40
        self.c = (self.x - 40)//40
        self.maze = Maze(self)
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

    def animate(self, delta):
        if self.isAtCenter():
            # r = self.r
            # c = self.c
            # if self.hasCoinAt(r,c)
            x = self.x
            y = self.y
            if self.maze.canMoveInDirection(x,y,Player.NEXT_DELTA_X,Player.NEXT_DELTA_Y):
                Player.DELTA_X = Player.NEXT_DELTA_X
                Player.DELTA_Y = Player.NEXT_DELTA_Y
            else:
                Player.DELTA_X = 0
                Player.DELTA_Y = 0
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


class Maze():
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

    def __init__(self, world):
        self.world = world
    def hasWallAt(self,r,c):
        return Maze.MAP[r] [c] == "x"

    def canMoveInDirection(self,x,y,dx,dy):

        row = (600 - 80 - y)//40
        column = (x - 40)//40
        newrow = row - dy
        newcolumn = column + dx
        if not self.hasWallAt(newrow,newcolumn):
            return 1 == 1

    def hasCoinAt(self,r,c):
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
        self.is_collected = False


    def hit(self, player):
        return (self.x == player.x) and (self.y == player.y)

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = Maze(self)
        self.speed = 5
        self.player = Player(self,80, 80)
        self.wall = []
        self.coins = []
        self.score = 0
        for r in range(self.maze.height):
            c = 0
            for letter in self.maze.MAP[r]:
                    x = c * 40 + 40
                    y = self.height - (r * 40) - 80
                    if self.maze.hasWallAt(r,c):
                        wall = Wall(self,x,y)
                        self.wall.append(wall)
                    if self.maze.hasCoinAt(r,c):
                            coin = Coin(self,x,y)
                            self.coins.append(coin)
                    c += 1


    def animate(self, delta):
        self.player.animate(delta)
        self.collect_coins()
    def collect_coins(self):
        for c in self.coins:
            if (not c.is_collected) and (c.hit(self.player)):
                c.is_collected = True
                self.score += 1

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

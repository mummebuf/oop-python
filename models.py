import arcade.key
import random
ENEMYSPEED = 4

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


class Enemy():

    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.maze = Maze(self)
        self.random = 1
        self.next_delta_x = 0
        self.next_delta_y = 1
        self.delta_x = 1
        self.delta_y = 0
    def isAtCenter(self):
        return (self.x % 40) == 0 and (self.y % 40) == 0

    def gameOver(self, player):
        return ((abs(self.x - player.x) < 12) and
                        (abs(self.y - player.y) < 12))

    def setNextDirectionUp(self):
        self.next_delta_x = 0
        self.next_delta_y = 1

    def setNextDirectionDown(self):
        self.next_delta_x = 0
        self.next_delta_y = -1

    def setNextDirectionRight(self):
        self.next_delta_x = 1
        self.next_delta_y = 0

    def setNextDirectionLeft(self):
        self.next_delta_x = -1
        self.next_delta_y = 0

    def setNextDirectionDone(self):
        self.next_delta_x = 0
        self.next_delta_y = 0

    def animate(self, delta):
        self.x += self.delta_x * ENEMYSPEED
        self.y += self.delta_y * ENEMYSPEED
        if self.isAtCenter():
            x = self.x
            y = self.y
            if self.maze.canMoveInDirection(x,y,self.next_delta_x,self.next_delta_y):
                self.delta_x = self.next_delta_x
                self.delta_y = self.next_delta_y

                if self.random == 1 or self.random == 2:
                    self.random = random.randrange(3,5)

                    if self.random == 3:
                        self.setNextDirectionLeft()

                    if self.random == 4:
                        self.setNextDirectionRight()

                elif self.random == 3 or self.random == 4:
                    self.random = random.randrange(1,3)
                    if self.random == 1:
                        self.setNextDirectionUp()

                    if self.random == 2:
                        self.setNextDirectionDown()


            if not self.maze.canMoveInDirection(x,y,self.delta_x,self.delta_y):
                self.delta_x = 0
                self.delta_y = 0
                while not (self.maze.canMoveInDirection(x,y,self.next_delta_x,self.next_delta_y)):

                    if self.random == 1 or self.random ==2:
                        self.random = random.randrange(3,5)

                        if self.random == 3:
                            self.setNextDirectionLeft()
                        if self.random == 4:
                            self.setNextDirectionRight()


                    elif self.random == 3 or self.random ==4:
                        self.random = random.randrange(1,3)

                        if self.random == 1:
                            self.setNextDirectionUp()
                        if self.random == 2:
                            self.setNextDirectionDown()

class Maze():
    MAP = [ "xxxxxxxxxxxxxxxxxxxx",
            "x..................x",
            "x.xxx.x.x..x.x.xxx.x",
            "x.x.....x....x.....x",
            "x...x.x.x.xx.x.x.x.x",
            "x.x.x..........x.x.x",
            "x.....xxx..xx.x*...x",
            "x.x.x..........x.x.x",
            "x.x.x.x.xx.x.x.x.x.x",
            "x.....x......x...x.x",
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
    def hasEndAt(self,r,c):
        return Maze.MAP[r] [c] == "*"

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

class End:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def youWin(self, player):
        return (self.x == player.x) and (self.y == player.y)

class World:
    NUM_ENEMY = 2
    GAMEOVER = 0
    WIN = 0
    WINSCORE = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = Maze(self)
        self.speed = 8
        self.player = Player(self,80, 80)
        self.enemies = []
        for i in range(World.NUM_ENEMY):
            enemy = Enemy(self, 120, 80)
            self.enemies.append(enemy)
        self.wall = []
        self.coins = []
        self.ends = []
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
                    if self.maze.hasEndAt(r,c):
                        end = End(self,x,y)
                        self.ends.append(end)
                    c += 1

    def animate(self, delta):
        self.player.animate(delta)

        for enemy in self.enemies:
            enemy.animate(delta)

        self.collect_coins()
        self.updatespeed()
        self.add_enemy(self)
        self.GameOver()
        self.spamEnemy()
        self.win()

    def collect_coins(self):
        for c in self.coins:
            if (not c.is_collected) and (c.hit(self.player)):
                c.is_collected = True
                self.score += 10

    def win(self):
        if(World.WIN == 1):
             self.score = World.WINSCORE
        for end in self.ends:
            if (end.youWin(self.player)) and (World.WIN == 0) and (World.GAMEOVER == 0):
                World.WIN = 1
                World.WINSCORE = self.score
                print('Win')

    def GameOver(self):
        for enemy in self.enemies:
            if enemy.gameOver(self.player) and (World.WIN == 0) :
                World.GAMEOVER = 1
                self.score = 0

    def spamEnemy(self):
        if(World.GAMEOVER == 1) and World.WIN == 0 and len(self.enemies) < 300:
            topleftenemy = Enemy(self, 120, 480)
            toprightenemy = Enemy(self, 720, 480)
            botleftenemy = Enemy(self, 120, 80)
            botrightenemy = Enemy(self, 720, 80)
            centerenemy = Enemy(self, 420, 280)
            self.enemies.append(toprightenemy)
            self.enemies.append(topleftenemy)
            self.enemies.append(botleftenemy)
            self.enemies.append(botrightenemy)
            self.enemies.append(centerenemy)

    def add_enemy(self,world):
        if (self.score % 100 == 0) and (not self.score == 0):
            self.score += 10
            enemy = Enemy(self, 120, 80)
            self.enemies.append(enemy)

    def updatespeed(self):
        if self.score == 100:
            self.speed = 8
        if self.score == 300:
            self.speed = 4
        if self.score == 600:
            self.speed = 2
        if self.score == 1000:
            self.speed = 1

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

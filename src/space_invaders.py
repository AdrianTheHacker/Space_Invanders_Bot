from random import randint


class SpaceInvaders():
    def __init__(self, width, height):
        self.game_screen = []
        self.WIDTH = width
        self.HEIGHT = height

        self.ship = [4, 0]
        self.score = 0
        self.enemies = []

        for row in range(self.WIDTH): 
            row = []
            for pixel in range(self.HEIGHT):
                row.append('0')
            self.game_screen.append(row)

        self.game_screen[self.ship[0]][self.ship[1]] = '>'


    def get_next_move(self):
        next_move = input("Next Move: ")

        self.game_screen[self.ship[0]][self.ship[1]] = '0'

        char = '>'
        match next_move.lower():
            case 'w':
                self.ship[0] -= 1
                char = '^'

            case 'a':
                self.ship[1] -= 1
                char = '<'

            case 's':
                self.ship[0] += 1
                char = 'v'

            case 'd':
                self.ship[1] += 1
                char = '>'

            case other:
                pass

        self.game_screen[self.ship[0]][self.ship[1]] = char


    def add_enemies(self):
        if self.score % 5 == 0:
            self.enemies.append([randint(0, self.WIDTH - 1), -1])

    
    def draw_enemies(self):
        self.add_enemies()

        for enemy in self.enemies:
            self.game_screen[enemy[0]][enemy[1]] = '0'

            if enemy[1] != (len(self.game_screen) - 1)  * -1:
                enemy[1] -= 1

            else: 
                enemy[1] = len(self.game_screen[1]) - 1
            
            self.game_screen[enemy[0]][enemy[1]] = "X"


    def check_collision(self) -> bool:
        for enemy in self.enemies:
            if self.ship[0] == enemy[0] and self.ship[1] == enemy[1]:
                return True

        return False


    def run(self):

        while True:
            for row in self.game_screen:
                print(row)

            if self.check_collision() == True:
                print("Game Over")
                break

            self.get_next_move()
            self.draw_enemies()

            self.score += 0.5

import random


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:
    width = 40
    height = 40
    snake = [Coord(20, 20)]
    direction = "North"

    def initialize(self):
        random.seed()

    # responsible for moving the snake forwards depending on the direction
    def advance(self):
        first = self.snake[-1]
        last = self.snake[0]
        if self.direction == "North":
            self.snake.append[Coord(first.x, first.y + 1)]
            self.snake.remove(last)
        elif self.direction == "South":
            self.snake.append[Coord(first.x, first.y - 1)]
            self.snake.remove(last)
        elif self.direction == "East":
            self.snake.append[Coord(first.x + 1, first.y)]
            self.snake.remove(last)
        elif self.direction == "West":
            self.snake.append[Coord(first.x - 1, first.y)]
            self.snake.remove(last)

    # checking if the head has collided with its body or is out of bounds
    def collide(self):
        head = self.snake[-1]
        return head in self.snake[0:-1] or head.x < 0 or head.x >= self.width or head.y < 0 or head.y >= self.height

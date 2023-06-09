import random
import pygame


class Obstacle:
    def __init__(self, quarter, background):
        if quarter == 1:
            self.x = random.randint(2, 17) * 10
            self.y = random.randint(2, 17) * 10
        elif quarter == 2:
            self.x = random.randint(22, 33) * 10
            self.y = random.randint(2, 17) * 10
        elif quarter == 3:
            self.x = random.randint(2, 17) * 10
            self.y = random.randint(22, 33) * 10
        elif quarter == 4:
            self.x = random.randint(22, 33) * 10
            self.y = random.randint(22, 33) * 10

        self.height = random.randint(1, 5) * 10
        self.width = random.randint(1, 5) * 10
        self.color = (128, 128, 128)
        self.background = background

    def __paint_rect(self):
        return self.x, self.y, self.width, self.height

    def paint(self):
        pygame.draw.rect(self.background, self.color, (self.__paint_rect()))

    def coords(self):
        coord = []
        for x in range(self.x, self.x + self.width, 10):
            for y in range(self.y, self.y + self.height, 10):
                coord.append((x, y))

        return coord
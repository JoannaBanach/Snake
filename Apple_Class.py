import random
import pygame


class Apple:
    def __init__(self, background, if_green_apple: bool, **kwargs):
        self.x = random.randint(1, 38) * 10
        self.y = random.randint(1, 38) * 10
        self.height = 10
        self.width = 10
        self.color = (255, 0, 0)
        self.background = background
        self.if_green_apple = if_green_apple

        coords_occupied = []
        for arg_name, arg_value in zip(kwargs.keys(), kwargs.values()):
            if arg_name in ['obstacles_coords', 'apples']:
                coords_occupied = [*coords_occupied, *arg_value]

        while self.coord() in coords_occupied:
            self.x = random.randint(1, 38) * 10
            self.y = random.randint(1, 38) * 10

    def __paint_rect(self):
        return self.x, self.y, self.width, self.height

    def paint(self):
        pygame.draw.rect(self.background, self.color, (self.__paint_rect()))

    def coord(self):
        coord = (self.x, self.y)
        return coord

    def update(self, snake_coords, **kwargs):
        old_coord = self.coord()
        coords_occupied = snake_coords
        for arg_name, arg_value in zip(kwargs.keys(), kwargs.values()):
            if arg_name in ['obstacles_coords', 'apples']:
                coords_occupied = [*coords_occupied, *arg_value]
            elif arg_name == 'snake_length' and self.if_green_apple:
                if arg_value % 10 == 9:
                    self.color = (0, 255, 0)
                else:
                    self.color = (255, 0, 0)

        while self.coord() in coords_occupied or self.coord() == old_coord:
            self.x = random.randint(1, 38) * 10
            self.y = random.randint(1, 38) * 10

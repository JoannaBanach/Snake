import pygame


class SnakePart:
    def __init__(self, x, y, background):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 10
        self.color = (150, 75, 0)
        self.color_second = (0, 0, 0)
        self.background = background

    def __paint_rect(self):
        return self.x, self.y, self.width, self.height

    def __paint_circle(self):
        return self.x + 5, self.y + 5

    def coord(self):
        coord = (self.x, self.y)
        return coord

    def paint(self):
        pygame.draw.rect(self.background, self.color, (self.__paint_rect()))
        pygame.draw.circle(self.background, self.color_second, (self.__paint_circle()), 3)


class Snake:

    def __init__(self, background, if_walls: bool, if_green_apple: bool):
        self.x_delta = 10
        self.y_delta = 0
        self.background = background
        self.elements = [SnakePart(200, 200, self.background), SnakePart(190, 200, self.background)]
        self.if_walls = if_walls
        self.if_green_apple = if_green_apple

    def kill(self):
        del self

    def paint(self):
        for part in self.elements:
            part.paint()

    def increase(self):
        x = self.elements[-1].coord()[0] + self.x_delta
        y = self.elements[-1].coord()[1] + self.y_delta
        self.elements.append(SnakePart(x, y, self.background))

    def length(self):
        return len(self.elements)

    def coords(self):
        coord = []
        for part in self.elements:
            coord.append(part.coord())
        return coord

    def speed(self):
        return [self.x_delta, self.y_delta]

    def new_head(self):
        if self.if_walls:
            new_x = self.elements[0].x + self.x_delta
            new_y = self.elements[0].y + self.y_delta
            return new_x, new_y
        else:
            if self.elements[0].x + self.x_delta > 390:
                new_x = 0
            elif self.elements[0].x + self.x_delta < 0:
                new_x = 390
            else:
                new_x = self.elements[0].x + self.x_delta

            if self.elements[0].y + self.y_delta > 390:
                new_y = 0
            elif self.elements[0].y + self.y_delta < 0:
                new_y = 390
            else:
                new_y = self.elements[0].y + self.y_delta
            return new_x, new_y

    def update(self, apples=None, **kwargs):
        coords_occupied = self.coords()
        obstacle_coords = False
        for arg_name, arg_value in zip(kwargs.keys(), kwargs.values()):
            if arg_name == 'obstacles_coords':
                obstacle_coords = arg_value
                coords_occupied = [*coords_occupied, *arg_value]

        new_x, new_y = self.new_head()
        if (new_x, new_y) in coords_occupied or \
                (self.if_walls and (new_x < 10 or new_x >= 390 or
                                    new_y < 10 or new_y >= 390)):
            return True

        else:

            for i in range(len(apples)):
                if new_x == apples[i].x and new_y == apples[i].y:
                    apple_color = apples[i].check_color()
                    if apple_color[0] == 255 and apple_color[1] == 0 \
                            and apple_color[2] == 0:
                        self.increase()
                    else:
                        for j in range(3):
                            self.increase()

                    if obstacle_coords:
                        apples[i].update(self.coords(), snake_length=self.length(), obstacles_coords=obstacle_coords)
                    else:
                        apples[i].update(self.coords(), snake_length=self.length())

            for ind in reversed(range(self.length())):
                if ind != 0:
                    self.elements[ind].x = self.elements[ind - 1].x
                    self.elements[ind].y = self.elements[ind - 1].y
                else:
                    self.elements[ind].x = new_x
                    self.elements[ind].y = new_y

            return False

    def update_delta(self, speed):
        self.x_delta = speed[0]
        self.y_delta = speed[1]

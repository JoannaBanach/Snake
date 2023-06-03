import pygame
import Apple_Class as ac
import Obstacle_Class as oc
import Snake as se
import threading


class SnakeGame:
    def __init__(self, controls_dict, level):
        self.FPS = 5
        self.window_width = 400
        self.window_height = 450
        self.window = (self.window_width, self.window_height)
        self.done = False
        self.score = 0
        self.controls_dict = controls_dict
        self.level = level
        self.area = (0, 0, 400, 400)
        self.FPS_acc = 0
        self.snake_exists = False

    def update_speed(self, move, snake_speed):

        x_delta = snake_speed[0]
        y_delta = snake_speed[1]

        if move == self.controls_dict['down'] and y_delta == 0:
            x_delta = 0
            y_delta = 10
            if self.level in ['Super Easy', 'Easy', 'Medium']:
                self.FPS = 5
            elif self.level == 'Hard':
                self.FPS = 5 + self.FPS_acc
            elif self.level == 'Super Hard':
                self.FPS = 5 * self.FPS_acc
        elif move == self.controls_dict['up'] and y_delta == 0:
            x_delta = 0
            y_delta = -10
            if self.level in ['Super Easy', 'Easy', 'Medium']:
                self.FPS = 5
            elif self.level == 'Hard':
                self.FPS = 5 + self.FPS_acc
            elif self.level == 'Super Hard':
                self.FPS = 5 * self.FPS_acc
        elif move == self.controls_dict['left'] and x_delta == 0:
            x_delta = -10
            y_delta = 0
            if self.level in ['Super Easy', 'Easy', 'Medium']:
                self.FPS = 5
            elif self.level == 'Hard':
                self.FPS = 5 + self.FPS_acc
            elif self.level == 'Super Hard':
                self.FPS = 5 * self.FPS_acc
        elif move == self.controls_dict['right'] and x_delta == 0:
            x_delta = 10
            y_delta = 0
            if self.level in ['Super Easy', 'Easy', 'Medium']:
                self.FPS = 5
            elif self.level == 'Hard':
                self.FPS = 5 + self.FPS_acc
            elif self.level == 'Super Hard':
                self.FPS = 5 * self.FPS_acc
        elif (move == self.controls_dict['down'] and y_delta == 10) or \
                (move == self.controls_dict['up'] and y_delta == -10) or \
                (move == self.controls_dict['left'] and x_delta == -10) or \
                (move == self.controls_dict['right'] and x_delta == 10):
            if self.level in ['Super Easy', 'Easy', 'Medium']:
                self.FPS = 10
            elif self.level == 'Hard':
                self.FPS = 10 + self.FPS_acc
            elif self.level == 'Super Hard':
                self.FPS = 5 * self.FPS_acc + 5

        return x_delta, y_delta

    def print_score(self, screen):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 410))

    def accelerate(self):
        if self.level == 'Hard':
            self.FPS_acc += 2
        elif self.level == 'Super Hard':
            self.FPS_acc *= 1.2
        if self.snake_exists:
            threading.Timer(15.0, self.accelerate).start()

    def start_game(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Snake')
        screen = pygame.display.set_mode(self.window)
        background = pygame.Surface(self.window)

        apples = []
        obstacle_coords = []
        if self.level == "Super Easy":
            apples_number = 5
            if_green_apple = False
            if_walls = False
            self.area = (0, 0, 400, 400)
        elif self.level == 'Easy':
            apples_number = 1
            if_green_apple = False
            if_walls = False
            self.area = (0, 0, 400, 400)
        elif self.level == 'Medium':
            apples_number = 1
            if_green_apple = True
            if_walls = True
            self.area = (10, 10, 380, 380)
        elif self.level == 'Hard':
            apples_number = 3
            if_green_apple = True
            if_walls = True
            self.area = (10, 10, 380, 380)
            obstacle1 = oc.Obstacle(1, background)
            obstacle2 = oc.Obstacle(2, background)
            obstacle3 = oc.Obstacle(3, background)
            obstacle4 = oc.Obstacle(4, background)
            obstacle_coords = obstacle1.coords() + obstacle2.coords() + obstacle3.coords() + obstacle4.coords()
        elif self.level == 'Super Hard':
            apples_number = 1
            if_green_apple = True
            if_walls = True
            self.FPS_acc = 1.1
            self.area = (10, 10, 380, 380)
            obstacle1 = oc.Obstacle(1, background)
            obstacle2 = oc.Obstacle(2, background)
            obstacle3 = oc.Obstacle(3, background)
            obstacle4 = oc.Obstacle(4, background)
            obstacle_coords = obstacle1.coords() + obstacle2.coords() + obstacle3.coords() + obstacle4.coords()

        for i in range(apples_number):
            if obstacle_coords:
                apples.append(ac.Apple(background, apples=apples, if_green_apple=if_green_apple,
                                       obstacles_coords=obstacle_coords))
            else:
                apples.append(ac.Apple(background, apples=apples, if_green_apple=if_green_apple))
        snake = se.Snake(background, if_walls=if_walls, if_green_apple=if_green_apple)
        self.snake_exists = True

        threading.Timer(10.0, self.accelerate).start()

        while not self.done:
            clock.tick(self.FPS)
            pygame.draw.rect(background, (255, 255, 255), self.area)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.KEYDOWN:
                    snake.update_delta(self.update_speed(event.key, snake.speed()))
                    break

            for i in range(len(apples)):
                apples[i].paint()
            if obstacle_coords:
                self.done = snake.update(apples=apples, obstacles_coords=obstacle_coords) \
                    if not self.done else self.done
            else:
                self.done = snake.update(apples=apples) if not self.done else self.done

            if obstacle_coords:
                obstacle1.paint()
                obstacle2.paint()
                obstacle3.paint()
                obstacle4.paint()

            snake.paint()
            for i in range(len(apples)):
                apples[i].paint()
            screen.blit(background, (0, 0))
            self.score = (snake.length() - 2) * 10
            self.print_score(screen)
            pygame.display.flip()

        pygame.quit()
        del snake
        self.snake_exists = False
        return self.score

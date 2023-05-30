import pygame_gui
import pygame
import Save_Score
import Snake_Game as sg


class SnakeGUI:
    def __init__(self):
        self.window_width = 600
        self.window_height = 400
        self.window = (self.window_width, self.window_height)
        self.done = False
        self.level = 'Easy'
        self.player_name = 'Nickname'
        self.controls = 'Arrows'
        self.controls_dict = {}
        self.run_game = False

    def start_game(self):
        if self.level in ['Super Easy', 'Easy', 'Medium', 'Hard', 'Super Hard']:
            snake = sg.SnakeGame(self.controls_dict, self.level)
        else:
            exit()
        score = snake.start_game()
        del snake
        self.end_window(score)

    def start_window(self):
        self.done = False
        self.run_game = False
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Snake start window')
        screen = pygame.display.set_mode(self.window)

        background = pygame.Surface(self.window)
        background.fill(pygame.Color('#C0C0C0'))

        manager = pygame_gui.UIManager(self.window)

        pygame_gui.elements.UITextBox(html_text='Snake',
                                      relative_rect=pygame.Rect((230, 40), (140, 30)),
                                      manager=manager)

        pygame_gui.elements.UITextBox(html_text='Provide your name',
                                      relative_rect=pygame.Rect((200, 70), (200, 30)),
                                      manager=manager)

        entryName = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((230, 100), (140, 30)),
                                                        initial_text=self.player_name,
                                                        manager=manager)

        pygame_gui.elements.UITextBox(html_text='Choose difficulty level',
                                      relative_rect=pygame.Rect((200, 140), (200, 30)),
                                      manager=manager)

        dropDownLevel = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect((200, 170), (200, 30)),
            options_list=['Super Easy', 'Easy', 'Medium', 'Hard', 'Super Hard'],
            starting_option=self.level,
            manager=manager)

        pygame_gui.elements.UITextBox(html_text='Choose controls',
                                      relative_rect=pygame.Rect((200, 200), (200, 30)),
                                      manager=manager)

        dropDownKeys = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect((200, 230), (200, 30)),
            options_list=['Arrows', 'WASD', 'IJKL', 'Num keyboard'],
            starting_option=self.controls,
            manager=manager)

        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((230, 300), (140, 50)),
                                              text='Start game',
                                              manager=manager)

        while not self.done:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                manager.process_events(event)

            if button.check_pressed():
                self.player_name = entryName.get_text()
                self.level = dropDownLevel.selected_option
                self.controls = dropDownKeys.selected_option
                self.done = True
                self.run_game = True

                if self.controls == 'Arrows':
                    self.controls_dict['up'] = pygame.K_UP
                    self.controls_dict['down'] = pygame.K_DOWN
                    self.controls_dict['left'] = pygame.K_LEFT
                    self.controls_dict['right'] = pygame.K_RIGHT
                elif self.controls == 'WASD':
                    self.controls_dict['up'] = pygame.K_w
                    self.controls_dict['down'] = pygame.K_s
                    self.controls_dict['left'] = pygame.K_a
                    self.controls_dict['right'] = pygame.K_d
                elif self.controls == 'IJKL':
                    self.controls_dict['up'] = pygame.K_i
                    self.controls_dict['down'] = pygame.K_k
                    self.controls_dict['left'] = pygame.K_j
                    self.controls_dict['right'] = pygame.K_l
                elif self.controls == 'Num keyboard':
                    self.controls_dict['up'] = pygame.K_KP8
                    self.controls_dict['down'] = pygame.K_KP2
                    self.controls_dict['left'] = pygame.K_KP4
                    self.controls_dict['right'] = pygame.K_KP6

            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.flip()

            if self.run_game:
                self.start_game()

        pygame.quit()

    def end_window(self, score):

        result_file = Save_Score.SaveScore()
        result_file.initiate_file()

        place = result_file.write_score(score, self.level, self.player_name)

        self.done = False
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Snake exit window')
        screen = pygame.display.set_mode(self.window)

        background = pygame.Surface(self.window)
        background.fill(pygame.Color('#C0C0C0'))

        manager = pygame_gui.UIManager(self.window)

        pygame_gui.elements.UITextBox(html_text='GAME OVER',
                                      relative_rect=pygame.Rect((230, 40), (140, 30)),
                                      manager=manager)

        pygame_gui.elements.UITextBox(html_text=f"Your score: {score}",
                                      relative_rect=pygame.Rect((230, 70), (140, 30)),
                                      manager=manager)

        if place < 11:
            last_text = "Your place: " + str(place)
        else:
            last_text = "Result out of scoreboard"

        pygame_gui.elements.UITextBox(html_text=last_text,
                                      relative_rect=pygame.Rect((175, 100), (250, 30)),
                                      manager=manager)

        button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((175, 200), (250, 50)),
                                              text='Back to main window',
                                              manager=manager)

        while not self.done:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                manager.process_events(event)

            if button.check_pressed():
                self.done = True
                self.start_window()
                break

            manager.update(time_delta)
            screen.blit(background, (0, 0))
            manager.draw_ui(screen)
            pygame.display.flip()

        pygame.quit()

""" Hangman game """

import random
import pygame
import sys
import time
import re
import requests

# Constants for colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (190, 255, 150)
BLUE = (0, 0, 225)
CREAM = (255, 220, 200)
GREY = (200, 200, 200)
PURPLE = (150, 0, 255)
LEFT_CLICK = (1, 0, 0)
RIGHT_CLICK = (0, 0, 1)
DARK_GREEN = (17, 51, 0)
CERULEAN = (0, 64, 128)
NEON_GREEN = (179, 255, 25)

# Constants for fonts and sounds
FONT_PATH = "Games/Hangman/FreeSansBoldOblique-BYJ3.otf"
FONT2_PATH = "Games/Hangman/PartyConfettiRegular-eZOn3.ttf"
BACKGROUND_MUSIC_PATH = "Games/Hangman/background_music.wav"
KEYBOARD_SOUND_PATH = "Games/Hangman/Keyboard.wav"
MOUSE_CLICK_SOUND_PATH = "Games/Hangman/mouse-click.wav"
GAME_OVER_SOUND_PATH = "Games/Hangman/game-over.wav"


class HangmanGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Hangman")
        self.display = pygame.display.set_mode((1000, 600), 0, 32)
        self.background_image = pygame.image.load("Games/Hangman/clouds.png")
        self.background_image = pygame.transform.scale(self.background_image, (1200, 600))
        self.font = pygame.font.Font(FONT_PATH, 50)
        self.font2 = pygame.font.Font(FONT2_PATH, 40)

    def get_word(self):
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        WORDS = response.content.splitlines()
        random_index = random.randint(0, len(WORDS))
        return WORDS[random_index].decode()

    def hangman(self, condition):
        if condition == 0:
            self.display.blit(self.font.render(" ", True, CERULEAN), (400, 350))
        elif condition == 1:
            self.display.blit(self.font.render("H ", True, BLACK), (400, 350))
        elif condition == 2:
            self.display.blit(self.font.render("A ", True, BLACK), (449, 350))
        elif condition == 3:
            self.display.blit(self.font.render("N ", True, BLACK), (498, 350))
        elif condition == 4:
            self.display.blit(self.font.render("G ", True, BLACK), (547, 350))
        elif condition == 5:
            self.display.blit(self.font.render("M ", True, BLACK), (596, 350))
        elif condition == 6:
            self.display.blit(self.font.render("A ", True, BLACK), (645, 350))
        elif condition == 7:
            self.display.blit(self.font.render("N", True, BLACK), (694, 350))

    def start_screen(self):
        self.display.blit(pygame.font.Font(FONT_PATH, 70).render("HANGMAN", True, PURPLE), (249, 40))
        self.display.blit(self.font2.render("PRESS 'ENTER' TO CONTINUE", True, DARK_GREEN), (232, 170))
        pygame.display.update()

    def start_hangman(self):
        TheWord = self.get_word()
        self.display.blit(self.background_image, (0, 0))

        TheChoice = 0

        self.start_screen()

        # background music
        pygame.mixer.music.load(BACKGROUND_MUSIC_PATH)
        pygame.mixer.music.play(-1, 0)

        FirstCondi = True
        while FirstCondi:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        FirstCondi = False
                        self.display.blit(self.background_image, (0, 0))
                        break

            pygame.display.update()
            pygame.time.Clock().tick(30)  # 30fps

        EmptyList = ['-'] * len(TheWord)

        Hidden = self.font.render("".join(EmptyList), True, NEON_GREEN)
        HiddenRect = Hidden.get_rect()
        HiddenRect.center = (350, 250)
        self.display.blit(Hidden, HiddenRect)

        Condition = 0  # if condition is 7, then end game

        Off = 0  # quit game at game over and congrats
        Start = time.time()  # current time

        LastKeyPressed = ""

        while True:
            self.hangman(Condition)
            End = time.time()  # end time
            if int(End) - int(Start) == 1:
                Start = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound(KEYBOARD_SOUND_PATH).play()

                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        continue

                    LastKeyPressed = event.key
                    self.display.blit(self.background_image.subsurface((220, 200, 280, 100)), (220, 200))  # hide word
                    self.display.blit(self.background_image.subsurface((50, 50, 50, 50)), (60, 150))  # hide invalid input
                    UserInput = event.key

                    if re.search("[a-z]", chr(event.key)):
                        if (chr(event.key).upper() in TheWord) or (chr(event.key).lower() in TheWord):
                            for i in range(len(TheWord)):
                                if (TheWord[i] == (chr(event.key)).upper()) or (TheWord[i] == (chr(event.key)).lower()):
                                    EmptyList[i] = TheWord[i]
                        else:
                            Condition += 1

                        Hidden = self.font.render("".join(EmptyList), True, NEON_GREEN)
                        HiddenRect = Hidden.get_rect()
                        HiddenRect.center = (350, 250)
                        self.display.blit(Hidden, HiddenRect)
                    else:
                        self.display.blit(Hidden, HiddenRect)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed() != (0, 0, 0):
                        pygame.mixer.Sound(MOUSE_CLICK_SOUND_PATH).play()

            if Condition == 7:
                self.display.blit(self.background_image, (0, 0))
                self.hangman(Condition + 1)
                Over = self.font2.render("GAME OVER!!!", True, RED)
                OverRect = Over.get_rect()
                OverRect.center = (360, 190)
                self.display.blit(Over, OverRect)

                FinalWord = self.font2.render("The word was: " + TheWord, True, BLACK)
                FinalWordRect = FinalWord.get_rect()
                FinalWordRect.center = (365, 240)
                self.display.blit(FinalWord, FinalWordRect)

                Off = 1

                pygame.mixer.music.stop()
                pygame.mixer.music.load(GAME_OVER_SOUND_PATH)
                pygame.mixer.music.play(0, 0)

            elif TheWord == "".join(EmptyList):
                self.display.blit(self.background_image, (0, 0))
                Cong = self.font.render("CONGRATS!!!", True, RED)
                CongRect = Cong.get_rect()
                CongRect.center = (340, 220)
                self.display.blit(Cong, CongRect)

                Word = self.font2.render("The word is:", True, BLACK)
                WordRect = Word.get_rect()
                WordRect.center = (340, 270)
                self.display.blit(Word, WordRect)

                Word2 = self.font.render(TheWord, True, BLACK)
                Word2Rect = Word2.get_rect()
                Word2Rect.center = (340, 305)
                self.display.blit(Word2, Word2Rect)

                Off = 1

                pygame.mixer.music.stop()
                pygame.mixer.music.load(GAME_OVER_SOUND_PATH)
                pygame.mixer.music.play(0, 0)

            pygame.display.update()
            pygame.time.Clock().tick(30)  # 30fps

            if Off == 1:
                time.sleep(5)
                break




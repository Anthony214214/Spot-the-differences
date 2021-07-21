from sprites import *
from game import *
import pygame
from PIL import Image

DISTANCE = 270
MATERIAL_PATH = "./game_material/"


class Level(object):
    def __init__(self, number):
        super(Level, self).__init__()
        self.characters = []
        self.characters_m = []
        self.inter_character = []
        self.circles = []
        self.bars = []
        self.num = number
        self.is_found = 0
        self.is_passed = 0
        self.is_lose = 0
        self.is_retry = 0

    def create_elements(self, elements):
        for element in elements:
            self.characters.append(ImageSprite(MATERIAL_PATH + element))

    def set_diffs(self):
        pass

    def update_positions(self, positions):
        i = 0
        for position in positions:
            self.characters[i].update(position[0], position[1])
            self.characters_m[i].update(position[0], position[1] + DISTANCE)
            i += 1

    def if_in_rect(self, pos_x, pos_y):
        i = 0
        j = 0
        while i < self.num:
            con = (self.inter_character[j].is_in_rect(pos_x, pos_y)) | (self.inter_character[j + 1].is_in_rect(
                pos_x, pos_y))
            if con == 1:
                self.is_found += 1
                return i + 1
            i += 1
            j += 2
        return 0

    def create_circles(self):
        i = 0
        while i <= (self.num * 2 - 1):
            circle.resize("circle" + str(i) + ".png", self.inter_character[i].rect.width,
                          self.inter_character[i].rect.width)
            self.circles.append(ImageSprite(SAVE_PATH + "circle" + str(i) + ".png"))
            i += 1

    def update_circles(self):
        i = 0
        while i <= (self.num * 2 - 1):
            self.circles[i].update(self.inter_character[i].rect.x, self.inter_character[i].rect.y)
            i += 1

    def create_bars(self):
        i = 0
        while i <= 9:
            self.bars.append(ImageSprite(MATERIAL_PATH + "timebar" + str(i + 1) + ".png"))
            i += 1

    def update_bars(self):
        i = 0
        while i <= 9:
            self.bars[i].update(0, 260)
            i += 1


class Level1(Level):
    def __init__(self):
        super(Level1, self).__init__(number=4)

    def set_diffs(self):
        self.characters[0].resize("me_1.png", 120, 120)
        self.characters_m.append(ImageSprite(SAVE_PATH + "me_1.png"))
        self.characters[1].resize("mace_1.png", 80, 80)
        self.characters_m.append(ImageSprite(SAVE_PATH + "mace_1.png"))
        self.characters[2].get_surrounding_color(560, 201)
        self.characters[2].color("bush_1.png")
        self.characters_m.append(ImageSprite(SAVE_PATH + "bush_1.png"))
        self.characters_m.append(ImageSprite(MATERIAL_PATH + "cloud2.png"))
        self.inter_character = [self.characters[0], self.characters_m[0], self.characters[1], self.characters_m[1], self.characters[2], self.characters_m[2], self.characters[3], self.characters_m[3]]


class Level2(Level):
    def __init__(self):
        super(Level2, self).__init__(number=6)

    def set_diffs(self):
        ImageSprite(MATERIAL_PATH + "transparent.png").resize("lv2_1.png", self.characters[0].rect.width, self.characters[0].rect.height)
        self.characters_m.append(ImageSprite(SAVE_PATH + "lv2_1.png"))
        self.characters[1].resize("lv2_2.png", 50, 50)
        self.characters_m.append(ImageSprite(SAVE_PATH + "lv2_2.png"))
        self.characters_m.append(ImageSprite(MATERIAL_PATH + "coinm.png"))
        self.characters[3].rotate("lv2_4.png", 180)
        self.characters_m.append(ImageSprite(SAVE_PATH + "lv2_4.png"))
        self.characters_m.append(ImageSprite(MATERIAL_PATH + "orange_flower.png"))
        self.characters_m.append(ImageSprite(MATERIAL_PATH + "chest.png"))
        self.characters_m.append(ImageSprite(MATERIAL_PATH + "coin.png"))
        self.characters_m.append(ImageSprite(MATERIAL_PATH + "star.png"))
        self.inter_character = [self.characters[0], self.characters_m[0], self.characters[1], self.characters_m[1], self.characters[2], self.characters_m[2], self.characters[3], self.characters_m[3], self.characters[4], self.characters_m[4], self.characters[5], self.characters_m[5]]


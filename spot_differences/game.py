from sprites import *
from levels import *
import pygame
import time
from PIL import Image

SCREEN_RECT = pygame.Rect(0, 0, 720, 530)
FRAME_PER_SEC = 60
circle = ImageSprite("./game_material/circle.png")
ICON_X = 276
ICON_Y = 234
SIGN_X = 490
SIGN_Y = 370


class Game(object):

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        pygame.display.set_caption("Spot the Differences")
        self.clock = pygame.time.Clock()
        self.is_play = 0
        self.is_play2 = 0
        self.time_count = 0
        self.time_count2 = 0
        self.judge = 0
        self.judge2 = 0
        self.is_click1 = [0, 0, 0, 0]
        self.is_click2 = [0, 0, 0, 0, 0, 0]
        self.__create_sprites()

    def __create_sprites(self):
        self.menu = ImageSprite("./game_material/menu.png")
        self.play_icon = ImageSprite("./game_material/play_icon.png")
        self.lv1_sign = ImageSprite(MATERIAL_PATH + "lv1_sign.png")
        self.menu_group = pygame.sprite.Group(self.menu, self.play_icon, self.lv1_sign)
        self.bg0 = ImageSprite("./game_material/background.png")
        self.bg1 = ImageSprite("./game_material/background.png")
        self.shed = ImageSprite("./game_material/shed.png")
        self.bg_group = pygame.sprite.Group(self.bg0, self.bg1, self.shed)
        self.LV1 = Level1()
        self.LV1.create_elements(["me.png", "mace.png", "bush.png", "cloud1.png"])
        self.LV1.set_diffs()
        self.lv1_group0 = pygame.sprite.Group(self.LV1.characters[0], self.LV1.characters[1], self.LV1.characters[2],
                                              self.LV1.characters[3])
        self.lv1_group1 = pygame.sprite.Group(self.LV1.characters_m[0], self.LV1.characters_m[1],
                                              self.LV1.characters_m[2], self.LV1.characters_m[3])

        self.LV1.create_bars()
        self.bars_group = pygame.sprite.Group()

        self.LV1.create_circles()
        self.circle_group0 = pygame.sprite.Group(self.LV1.circles[0], self.LV1.circles[1])
        self.circle_group1 = pygame.sprite.Group(self.LV1.circles[2], self.LV1.circles[3])
        self.circle_group2 = pygame.sprite.Group(self.LV1.circles[4], self.LV1.circles[5])
        self.circle_group3 = pygame.sprite.Group(self.LV1.circles[6], self.LV1.circles[7])

        self.win = ImageSprite(MATERIAL_PATH + "win.png")
        self.continue_icon = ImageSprite(MATERIAL_PATH + "continue_icon.png")
        self.lv2_sign = ImageSprite(MATERIAL_PATH + "lv2_sign.png")
        self.win_group = pygame.sprite.Group(self.win, self.continue_icon, self.lv2_sign)

        self.lose = ImageSprite(MATERIAL_PATH + "lose.png")
        self.retry_icon = ImageSprite(MATERIAL_PATH + "retry_icon.png")
        self.lose_group = pygame.sprite.Group(self.lose, self.retry_icon)

        self.LV2 = Level2()
        self.bg2 = ImageSprite(MATERIAL_PATH + "new_background.png")
        self.bg3 = ImageSprite(MATERIAL_PATH + "new_background.png")
        self.bg_group2 = pygame.sprite.Group(self.bg2, self.bg3, self.shed)
        self.LV2.create_elements(
            ["cloud1.png", "cloud2.png", "coin.png", "star.png", "red_flower.png", "chest_open.png", "coin.png",
             "star.png"])
        self.LV2.set_diffs()
        self.lv2_group0 = pygame.sprite.Group()
        self.lv2_group1 = pygame.sprite.Group()
        for self.LV2.character in self.LV2.characters:
            self.lv2_group0.add(self.LV2.character)
        for self.LV2.character_m in self.LV2.characters_m:
            self.lv2_group1.add(self.LV2.character_m)

        self.LV2.create_bars()
        self.bars_group2 = pygame.sprite.Group()

        self.LV2.create_circles()
        self.circle_group4 = pygame.sprite.Group(self.LV2.circles[0], self.LV2.circles[1])
        self.circle_group5 = pygame.sprite.Group(self.LV2.circles[2], self.LV2.circles[3])
        self.circle_group6 = pygame.sprite.Group(self.LV2.circles[4], self.LV2.circles[5])
        self.circle_group7 = pygame.sprite.Group(self.LV2.circles[6], self.LV2.circles[7])
        self.circle_group8 = pygame.sprite.Group(self.LV2.circles[8], self.LV2.circles[9])
        self.circle_group9 = pygame.sprite.Group(self.LV2.circles[10], self.LV2.circles[11])

        self.thank_icon = ImageSprite(MATERIAL_PATH + "thank_icon.png")
        self.win2_group = pygame.sprite.Group(self.win, self.thank_icon)

    def start_game(self):
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__update_sprites()
            self.__event_handler()
            pygame.display.update()

    def __update_sprites(self):
        if self.is_play == 0:
            self.menu.update(0, 0)
            self.play_icon.update(ICON_X, ICON_Y)
            self.lv1_sign.update(SIGN_X, SIGN_Y)
            self.menu_group.draw(self.screen)

        if ((self.is_play == 1) and (self.is_play2 == 0)) or (self.LV1.is_retry == 1):
            self.bg0.update(0, 0)
            self.bg1.update(0, 270)
            self.shed.update(0, 260)
            self.bg_group.draw(self.screen)

            self.LV1.update_positions([(30, 100), (200, 2), (560, 200), (400, 0)])
            self.lv1_group0.draw(self.screen)
            self.lv1_group1.draw(self.screen)

            self.LV1.update_circles()
            self.LV1.update_bars()

            if (self.time_count > 0) and (self.LV1.is_passed == 0):
                if self.time_count == 1:
                    self.bars_group.add(self.LV1.bars[0])
                elif self.time_count == 2:
                    self.bars_group.add(self.LV1.bars[1])
                elif self.time_count == 3:
                    self.bars_group.add(self.LV1.bars[2])
                elif self.time_count == 4:
                    self.bars_group.add(self.LV1.bars[3])
                elif self.time_count == 5:
                    self.bars_group.add(self.LV1.bars[4])
                elif self.time_count == 6:
                    self.bars_group.add(self.LV1.bars[5])
                elif self.time_count == 7:
                    self.bars_group.add(self.LV1.bars[6])
                elif self.time_count == 8:
                    self.bars_group.add(self.LV1.bars[7])
                elif self.time_count == 9:
                    self.bars_group.add(self.LV1.bars[8])
                elif self.time_count == 10:
                    self.bars_group.add(self.LV1.bars[9])
                    self.LV1.is_lose = 1
                self.bars_group.draw(self.screen)

            if self.judge == 1 or self.is_click1[0] == 1:
                self.is_click1[0] = 1
                self.circle_group0.draw(self.screen)
            if self.judge == 2 or self.is_click1[1] == 1:
                self.is_click1[1] = 1
                self.circle_group1.draw(self.screen)
            if self.judge == 3 or self.is_click1[2] == 1:
                self.is_click1[2] = 1
                self.circle_group2.draw(self.screen)
            if self.judge == 4 or self.is_click1[3] == 1:
                self.is_click1[3] = 1
                self.circle_group3.draw(self.screen)

            if self.LV1.is_found == self.LV1.num:
                self.LV1.is_passed = 1
                self.LV1.is_retry = 0
                self.win.update(0, 0)
                self.continue_icon.update(ICON_X, ICON_Y)
                self.lv2_sign.update(SIGN_X, SIGN_Y)
                self.win_group.draw(self.screen)
            if self.LV1.is_lose == 1:
                self.lose.update(0, 0)
                self.retry_icon.update(ICON_X, ICON_Y)
                self.lose_group.draw(self.screen)

        if ((self.is_play2 == 1) and (self.LV1.is_passed == 1)) or (self.LV2.is_retry == 1):
            self.bg2.update(0, 0)
            self.bg3.update(0, 270)
            self.shed.update(0, 260)
            self.bg_group2.draw(self.screen)

            self.LV2.update_positions(
                [(150, 18), (418, 0), (478, 150), (87, 110), (648, 25), (536, 56), (510, 150), (308, 45)])
            self.lv2_group0.draw(self.screen)
            self.lv2_group1.draw(self.screen)

            self.LV2.update_circles()
            self.LV2.update_bars()

            if (self.time_count2 > 0) and (self.LV2.is_passed == 0):
                if self.time_count2 == 1:
                    self.bars_group2.add(self.LV2.bars[0])
                elif self.time_count2 == 2:
                    self.bars_group2.add(self.LV2.bars[1])
                elif self.time_count2 == 3:
                    self.bars_group2.add(self.LV2.bars[2])
                elif self.time_count2 == 4:
                    self.bars_group2.add(self.LV2.bars[3])
                elif self.time_count2 == 5:
                    self.bars_group2.add(self.LV2.bars[4])
                elif self.time_count2 == 6:
                    self.bars_group2.add(self.LV2.bars[5])
                elif self.time_count2 == 7:
                    self.bars_group2.add(self.LV2.bars[6])
                elif self.time_count2 == 8:
                    self.bars_group2.add(self.LV2.bars[7])
                elif self.time_count2 == 9:
                    self.bars_group2.add(self.LV2.bars[8])
                elif self.time_count2 == 10:
                    self.bars_group2.add(self.LV2.bars[9])
                    self.LV2.is_lose = 1
                self.bars_group2.draw(self.screen)

            if self.judge2 == 1 or self.is_click2[0] == 1:
                self.is_click2[0] = 1
                self.circle_group4.draw(self.screen)
            if self.judge2 == 2 or self.is_click2[1] == 1:
                self.is_click2[1] = 1
                self.circle_group5.draw(self.screen)
            if self.judge2 == 3 or self.is_click2[2] == 1:
                self.is_click2[2] = 1
                self.circle_group6.draw(self.screen)
            if self.judge2 == 4 or self.is_click2[3] == 1:
                self.is_click2[3] = 1
                self.circle_group7.draw(self.screen)
            if self.judge2 == 5 or self.is_click2[4] == 1:
                self.is_click2[4] = 1
                self.circle_group8.draw(self.screen)
            if self.judge2 == 6 or self.is_click2[5] == 1:
                self.is_click2[5] = 1
                self.circle_group9.draw(self.screen)

            if self.LV2.is_found == self.LV2.num:
                self.LV2.is_passed = 1
                self.LV2.is_retry = 0
                self.win.update(0, 0)
                self.thank_icon.update(ICON_X, ICON_Y)
                self.win2_group.draw(self.screen)
            if self.LV2.is_lose == 1:
                self.lose.update(0, 0)
                self.retry_icon.update(ICON_X, ICON_Y)
                self.lose_group.draw(self.screen)

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.__game_over()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_play == 0:
                    mx, my = pygame.mouse.get_pos()
                    self.is_play = self.play_icon.is_in_rect(mx, my)
                    if self.is_play == 1:
                        pygame.time.set_timer(COUNT1, 1000)
                if (self.is_play == 1) and (self.LV1.is_passed == 0):
                    x, y = pygame.mouse.get_pos()
                    self.judge = self.LV1.if_in_rect(x, y)
                if (self.LV1.is_passed == 1) and (self.is_play2 == 0):
                    x2, y2 = pygame.mouse.get_pos()
                    self.is_play2 = self.continue_icon.is_in_rect(x2, y2)
                    if self.is_play2 == 1:
                        pygame.time.set_timer(COUNT2, 1000)
                if self.LV1.is_lose == 1:
                    rx1, ry1 = pygame.mouse.get_pos()
                    self.LV1.is_retry = self.retry_icon.is_in_rect(rx1, ry1)
                    if self.LV1.is_retry == 1:
                        self.LV1.is_lose = 0
                        self.LV1.is_found = 0
                        self.judge = 0
                        self.bars_group = pygame.sprite.Group()
                        self.is_click1 = [0, 0, 0, 0]
                        self.time_count = 0
                if (self.is_play2 == 1) and (self.LV2.is_passed == 0):
                    xx, yy = pygame.mouse.get_pos()
                    self.judge2 = self.LV2.if_in_rect(xx, yy)
                if self.LV2.is_lose == 1:
                    rx2, ry2 = pygame.mouse.get_pos()
                    self.LV2.is_retry = self.retry_icon.is_in_rect(rx2, ry2)
                    if self.LV2.is_retry == 1:
                        self.LV2.is_lose = 0
                        self.LV2.is_found = 0
                        self.judge2 = 0
                        self.bars_group2 = pygame.sprite.Group()
                        self.is_click2 = [0, 0, 0, 0, 0, 0]
                        self.time_count2 = 0
                if self.LV2.is_passed == 1:
                    tx, ty = pygame.mouse.get_pos()
                    if self.thank_icon.is_in_rect(tx, ty):
                        Game().__game_over()
            if event.type == COUNT1:
                self.time_count += 1
            if event.type == COUNT2:
                self.time_count2 += 1

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    spot_diffs = Game()
    spot_diffs.start_game()

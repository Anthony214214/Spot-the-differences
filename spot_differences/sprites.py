from PIL import Image
import pygame
import random

SAVE_PATH = "./modified_sprites/"
COUNT1 = pygame.USEREVENT + 1
COUNT2 = pygame.USEREVENT + 2


class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, name):
        super(ImageSprite, self).__init__()
        self.name = name
        self.image = pygame.image.load(self.name)
        self.rect = self.image.get_rect()
        self.sr = 0
        self.sg = 0
        self.sb = 0

    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def resize(self, new_name, new_x, new_y):
        img = Image.open(self.name)
        img_diff = img.resize((new_x, new_y))
        img_diff.save(SAVE_PATH + new_name)

    def rotate(self, new_name, angle):
        img = Image.open(self.name)
        img_diff = img.rotate(angle)
        img_diff.save(SAVE_PATH + new_name)

    def get_surrounding_color(self, pos_x, pos_y):
        img = Image.open("./game_material/background.png")
        self.sr, self.sg, self.sb, alpha = img.getpixel((pos_x, pos_y))

    def color(self, new_name):
        img = Image.open(self.name)
        r0, g0, b0, alpha0 = img.getpixel((self.rect.width * 0.5, self.rect.height * 0.5))
        for i in range(self.rect.width):
            for j in range(self.rect.height):
                try:
                    r, g, b, alpha = img.getpixel((i, j))
                    if r == r0 and g == g0 and b == b0:
                        r = self.sr
                        g = self.sg
                        b = self.sb
                        img.putpixel((i, j), (r, g, b, alpha))
                except Exception as e:
                    continue
        img.save(SAVE_PATH + new_name)

    def replace(self, new_name):
        img = Image.open("./game_material/" + new_name)
        img.save(SAVE_PATH + new_name)

    def dele(self, new_name):
        img = Image.open("./game_material/transparent.png")
        img = img.resize((self.rect.width, self.rect.height))
        img.save(SAVE_PATH + new_name)

    def is_in_rect(self, mx, my):
        condition = ((mx >= self.rect.x) & (mx <= self.rect.x + self.rect.width) & (my >= self.rect.y) & (
                my <= self.rect.y + self.rect.height))
        return condition

